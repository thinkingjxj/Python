from wsgiref.simple_server import make_server
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
            raise AttributeError('Attribute {} Not Found'.format(item))

    def __setattr__(self, key, value):
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
        self.globalcontext = globalcontext

    def relate(self, globalcontext: Context = None):
        self.globalcontext = globalcontext

    def __getattr__(self, item):
        if item in self.keys():
            return self[item]
        return self.globalcontext


class Router:
    KVPATERN = re.compile('/({[^{}:]+:?[^{}:]*})')

    TypePatterns = {
        'str': r'[^/]+',
        'word': r'\w+',
        'int': r'[+-]?\d+',
        'float': r'[+-]?\d+\.\d+',
        'any': r'.+'
    }

    TypeCast = {
        'str': str,
        'word': str,
        'int': int,
        'float': float,
        'any': str
    }

    def transform(self, kv: str):
        # /{id:int} => /(?P<id>[+-]?\d+)
        name, _, type = kv.strip('/{}').partition(':')
        # 返回元组，（目标正则表达式，被替换部分类型有序列表）
        return '/(?P<{}>{})'.format(name, self.TypePatterns.get(type, '\w+')), \
               name, self.TypeCast.get(type, str)

    def parse(self, src: str):

        start = 0
        res = ''
        translator = {}  # id=>int  name=>str
        while True:
            matcher = self.KVPATERN.search(src, start)
            if matcher:
                res += matcher.string[start:matcher.start()]
                tmp = self.transform(matcher.string[matcher.start():matcher.end()])
                res += tmp[0]
                translator[tmp[1]] = tmp[2]
                start = matcher.end()
            else:
                break
        # 没有任何匹配应该原样返回字符串
        if res:
            return res, translator
        else:
            return src, translator

    def __init__(self, prefix: str = ''):
        # URL: /product
        self.__prefix = prefix.rstrip('/\\')
        self.__routable = []

        # 上下文
        self.ctx = NestedContext()  # 未关联全局，注册时注入
        # 拦截器
        self.preinterceptor = []
        self.postinterceptor = []

    def reg_preinterceptor(self, fn):
        self.preinterceptor.append(fn)
        return fn

    def reg_postinterceptor(self, fn):
        self.postinterceptor.append(fn)
        return fn

    def route(self, rule, *methods):
        def wrapper(handler):
            pattern, translator = self.parse(rule)
            self.__routable.append((methods, re.compile(pattern), translator, handler))
            return handler

        return wrapper

    def get(self, pattern):
        return self.route(pattern, 'GET')

    def post(self, pattern):
        return self.route(pattern, 'POST')

    def head(self, pattern):
        return self.route(pattern, 'HEAD')

    def match(self, request: Request):
        if not request.path.startswith(self.__prefix):
            return
        # 依次执行拦截请求
        for fn in self.preinterceptor:
            request = fn(self.ctx, request)
        for methods, pattern, translator, handler in self.__routable:
            matcher = pattern.match(request.path.replace(self.__prefix, '', 1))
            if matcher:
                newdict = {}
                for k, v in matcher.groupdict().items():
                    newdict[k] = translator[k](v)
                request.vars = DictObj(newdict)  # request.vars.id   request.vars.name
                response = handler(self.ctx, request)
                # 依次执行拦截响应
                for fn in self.postinterceptor:
                    response = fn(self.ctx, request, response)
                # return handler(request)
                return response


class MagWeb:
    ROUTERS = []
    ctx = Context()
    # 拦截器
    PREINTERCEPTOR = []
    POSTINTERCEPTOR = []

    def __init__(self, **kwargs):
        # 创建上下文对象，共享信息
        self.ctx.app = self
        for k, v in kwargs:
            self.ctx[k] = v

    @classmethod
    def reg_PREINTERCEPTOR(cls, fn):
        cls.PREINTERCEPTOR.append(fn)
        return fn

    @classmethod
    def reg_POSTINTERCEPTOR(cls, fn):
        cls.POSTINTERCEPTOR.append(fn)
        return fn

    @classmethod
    def register(cls, router: Router):
        router.ctx.relate(cls.ctx)
        router.ctx.router = router
        cls.ROUTERS.append(router)

    @wsgify
    def __call__(self, request: Request):
        # 全局拦截请求
        for fn in self.PREINTERCEPTOR:
            request = fn(self.ctx, request)
        for router in self.ROUTERS:
            response = router.match(request)
            for fn in self.POSTINTERCEPTOR:
                response - fn(self.ctx, request, response)

            if response:
                return response
        raise exc.HTTPNotFound('<h1>您访问的页面被劫持了</h1>')


idx = Router()
py = Router('/python')

MagWeb.register(idx)
MagWeb.register(py)


@idx.get('^/$')  # 只匹配根
def index(request: Request) -> Response:
    res = Response()
    res.status_code = 200
    res.content_type = 'text/html'
    res.charset = 'utf-8'
    res.body = '<h1>Welcome to my world, please have fun.</h1>'
    return res


@py.route('/{id:int}')
def showpython(request: Request) -> Response:
    res = Response()
    res.content_type = 'text/plain'
    res.charset = 'utf-8'
    res.body = '<h1>Hello there, sunshine boys and beautiful girls, how are you?</h1>'
    return res


if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 9999
    server = make_server(ip, port, MagWeb())
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
