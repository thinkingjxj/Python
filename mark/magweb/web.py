from webob import Request, Response, exc
from webob.dec import wsgify
import re


class DictObj:
    def __init__(self, d: dict):
        if not isinstance(d, dict):
            self.__dict__['_dict'] = {}
        else:
            self.__dict__['_dict'] = d

    def __getattr__(self, item):
        try:
            return self._dict[item]
        except KeyError:
            raise AttributeError('Attribute {} Not found'.format(item))

    def __setattr__(self, key, value):
        # 不允许设置属性
        raise NotImplementedError


class Context(dict):
    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError('Attribute {} Not Found'.format(item))

    def __setattr__(self, key, value):
        self[key] = value


class NestedContext(Context):
    def __init__(self, globalcontext: Context = None):
        super().__init__()
        self.relate(globalcontext)

    def relate(self, globalcontext: Context = None):
        self.globalcontext = globalcontext

    def __getattr__(self, item):
        if item in self.keys():
            return self[item]
        return self.globalcontext[item]


class _Router:
    TYPEPATTERNS = {
        'str': r'[^/]+',
        'word': r'\w+',
        'int': r'[+-]?\d+',
        'float': r'[+-]?\d+\.\d+',
        'any': r'.+'
    }

    TYPECAST = {
        'str': str,
        'word': str,
        'int': int,
        'float': float,
        'any': str
    }

    KVPATTERN = re.compile(r'/([^{}:]+:?[^{}:]*)')

    def _transform(self, kv: str):
        # /{id:int} => /(?P<id>[+-]?\d+)
        name, _, type = kv.strip('/{}').partition(':')
        # 返回元组，（目标正则表达式，被替换部分类型有序列表）
        return '/(?P<{}>{})'.format(name, self.TYPEPATTERNS.get(type, '\w+')), \
               name, self.TYPECAST.get(type, str)

    def _parse(self, src: str):
        start = 0
        res = ''
        translator = {}  # id => int  name => str
        while True:
            matcher = self.KVPATTERN.search(src, start)
            if matcher:
                res += matcher.string[start:matcher.start()]
                tmp = self._transform(matcher.string[matcher.start():matcher.end()])

                res += tmp[0]
                translator[tmp[1]] = tmp[2]
                start = matcher.end()
            else:
                break
            # 没有任何匹配应该原样返回字符串 translator是字典
            if res:
                return res, translator
            else:
                return src, translator

    def __init__(self, prefix: str = ""):
        self._prefix = prefix.rstrip('/\\')  # 前缀，例如/product
        self._routetable = []  # 路由表

        # 拦截器
        self.pre_interceptor = []
        self.post_interceptor = []

        # 上下文
        self.ctx = NestedContext()  # 去关联全局，注册时注入

    @property
    def prefix(self):
        return self._prefix

    # 拦截器注册函数
    def register_preinterceptor(self, fn):
        self.pre_interceptor.append(fn)
        return fn

    def route(self, rule, *methods):  # 用户输入规则转换为pattern
        def wrapper(handler):
            # /student/{name:str}/xxx/{id:int} =>
            # ('/student/(?P<name>[^/]+)/xxx/(?P<id>[+-]?\\d+)', [<class 'str'>, <class 'int'>])
            pattern, translator = self._parse(rule)
            self._routetable.append((methods, re.compile(pattern), translator, handler))  # 四元组
            return handler

        return wrapper

    def get(cls, pattern):
        return cls.route(pattern, 'GET')

    def post(cls, pattern):
        return cls.route(pattern, 'POST')

    def head(cls, pattern):
        return cls.route(pattern, 'HEAD')

    def match(self, request: Request) -> Response:
        # 前缀处理，prefix是一级的
        if not request.path.startswith(self._prefix):
            return None

        # 依次执行拦截请求
        for fn in self.pre_interceptor:
            request = fn(self.ctx, request)

        for methods, pattern, translator, handler in self._routetable:
            # not methods表示一个方法都没有定义，就是支持全部方法
            if not methods or request.method.upper() in methods:
                # 保证是prefix开头，所以可以replace
                # 去掉prefix剩下的才是正则表达式匹配的路径
                matcher = pattern.match(request.path.replace(self._prefix, '', 1))
                if matcher:
                    newdict = {}
                    for k, v in matcher.groupdict().items():  # 命名分组组成的字典
                        newdict[k] = translator[k](v)  # 将id使用int转换
                    request.vars = DictObj(newdict)

                    # response = handler(request)
                    response = handler(self.ctx, request)  # 增加上下文

                    # 依次执行拦截响应
                    for fn in self.post_interceptor:
                        response = fn(self.ctx, request, response)
                    return response
        # 匹配不上返回None


class MagWeb:
    # 类属性方式把类暴露出去
    Router = _Router
    # Response, Request存在于此名词空间中，以后可以以：MagWeb.Request的方式使用
    Request = Request
    Response = Response

    ctx = Context()  # 全局上下文对象

    def __init__(self, **kwargs):
        self.ctx.app = self
        for k, v in kwargs:
            self.ctx[k] = v

    ROUTERS = []  # 前缀开头的所有Router对象

    # 拦截器注册函数
    PRE_INTERCEPTOR = []
    POST_INTERCEPTOR = []

    # 拦截器注册函数
    @classmethod
    def register_preinterceptor(cls, fn):
        cls.PRE_INTERCEPTOR.append(fn)
        return fn

    @classmethod
    def register_postinterceptor(cls, fn):
        cls.POST_INTERCEPTOR.append(fn)
        return fn

    @classmethod
    def register(cls, router: _Router):
        # 为Router实例注入全局上下文
        router.ctx.relate(cls.ctx)
        router.ctx.router = router
        cls.ROUTERS.append(router)

    @wsgify
    def __call__(self, request: Request) -> Response:
        # 全局拦截请求
        for fn in self.PRE_INTERCEPTOR:
            request = fn(self.ctx, request)

        # 遍历ROUTERS，调用Router实例的match方法，看谁匹配
        for router in self.ROUTERS:
            response = router.match(request)

            # 全局拦截响应
            for fn in self.POST_INTERCEPTOR:
                response = fn(self.ctx, request, response)

            if response:  # 匹配返回非None的Router对象
                return response
        raise exc.HTTPNotFound('<h1>您访问的页面被外星人劫持了</h1>')

    @classmethod
    def extend(cls, name, ext):
        cls.ctx[name] = ext
