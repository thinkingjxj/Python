from wsgiref.simple_server import make_server
from webob import Response, Request, exc
from webob.dec import wsgify
import re


class DictObj:
    def __init__(self, d: dict):
        if not isinstance(d, dict):
            self.__dict__['_dict'] = {}
        self.__dict__['_dict'] = d

    def __getattr__(self, item):
        try:
            return self._dict[item]
        except KeyError:
            raise AttributeError('Attribute {} Not Found'.format(item))

    def __setattr__(self, key, value):
        raise NotImplementedError


# 上下文信息类
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


class Router:
    pattern = re.compile('/({[^{}:]+:?}[^{}:]*})')

    # 类型字符串映射到正则表达式
    TYPEPATTERNS = {
        'str': r'[^/]+',
        'word': r'\w+',
        'int': r'[-+]?\d+',
        'float': r'[-+]\d+.\d+',
        'any': r'.+'
    }

    # 类型字符串到Python类型的映射
    TYPECAST = {
        'str': str,
        'word': str,
        'int': int,
        'float': float,
        'any': str
    }

    KVPATTERN = re.compile(r'/({[^{}:]+:?}[^{}:]*})')

    def transform(self, kv: str):
        # {id: int} => /(?P<id>[+-]?\d+)
        name, _, type = kv.strip('/{}').partition(':')
        return '/(?P<{}>{})'.format(name, self.TYPEPATTERNS.get(type, '\w+')), name, self.TYPECAST.get(type, str)

    def parse(self, src: str):
        start = 0
        res = ''
        translator = {}  # id=>int   name=>str
        while True:
            matcher = self.pattern.search(src, start)
            if matcher:
                res += matcher.string[start:matcher.start()]   # copy
                # tmp = transform(matcher.string[matcher.start():matcher.end()])
                # res += tmp[0]
                # translator[tmp[1]] = tmp[2]
                start = matcher.end()
            else:
                break
        if res:
            return res, translator
        else:
            return src, translator

    def __init__(self, prefix: str = ''):
        self._prefix = prefix.rstrip('/\\')
        self.Routbales = []

        # 拦截器
        self.pre_interceptor = []
        self.post_interceptor = []

        # 上下文
        self.ctx = NestedContext()  # 为关联全局，注册时注入

    @property
    def prefix(self):
        return self._prefix

    # 拦截器注册函数
    def register_preinterceptor(self, fn):
        self.pre_interceptor.append(fn)
        return fn

    def register_postinterceptor(self, fn):
        self.post_interceptor.append(fn)
        return fn

    def route(self, rule, *methods):
        def wrapper(handler):
            # self.Routbales.append((methods, re.compile(rule), handler))
            pattern, translator = self.parse(rule)
            self.Routbales.append((methods, re.compile(rule), translator, handler))

            return handler

        return wrapper

    def get(self, pattern):
        return self.route(pattern, 'GET')

    def post(self, pattern):
        return self.route(pattern, 'POST')

    def head(self, pattern):
        return self.route(pattern, 'HEAD')

    def match(self, request: Request):
        if not request.path.startswith(self._prefix):
            return
        # 依次执行拦截请求
        for fn in self.pre_interceptor:
            request = fn(self.ctx, request)

        for methods, pattern, translator, handler in self.Routbales:
            if not methods or request.method.upper() in methods:
                matcher = pattern.match(request.path.replace(self._prefix, '', 1))
                if matcher:
                    # request.args = matcher.group()
                    # request.kwargs = DictObj(matcher.groupdict())
                    # return handler(request)
                    newdict = {}
                    for k, v in matcher.groupdict().items():
                        newdict[k] = translator[k](v)
                    request.vars = DictObj(newdict)
                    response = handler(self.ctx, request)

                    # 依次执行拦截响应
                    for fn in self.post_interceptor:
                        response = fn(self.ctx, request, response)

                    return response


class Application:
    ROUTABLES = []
    ctx = Context()

    def __init__(self, **kwargs):
        self.ctx.app = self
        for k, v in kwargs:
            self.ctx[k] = v

    # 拦截器
    PREINTERCEPTOR = []
    POSTINTERCEPTOR = []

    @classmethod
    def register_preinterceptor(cls, fn):
        cls.PREINTERCEPTOR.append(fn)
        return fn

    @classmethod
    def register_postinterceptor(cls, fn):
        cls.POSTINTERCEPTOR.append(fn)
        return fn

    @classmethod
    def register(cls, router: Router):
        cls.ROUTABLES.append(router)

    @wsgify
    def __call__(self, request: Request):
        # 全局拦截器请求
        for fn in self.PREINTERCEPTOR:
            request = fn(self.ctx, request)

        for router in self.ROUTABLES:
            response = router.match(request)
            # 全局响应拦截
            for fn in self.POSTINTERCEPTOR:
                response = fn(self.ctx, request, response)

            if response:
                return response
        raise exc.HTTPNotFound('<h1>您访问的页面被外星人劫持了</h1>')


idx = Router()
py = Router('/python')

Application.register(idx)
Application.register(py)


@idx.get('^/$')
def index(request: Request) -> Response:
    res = Response()
    res.status_code = 200
    res.content_type = 'text/html'
    res.charset = 'utf-8'
    res.body = '<h1>Welcome to my world. Please enjoy youself.</h1>'
    return res


# @py.get('/{id:]')
# @py.get('{id}')
@py.get('/{id:int}')
# @py.route('/(\w+)')
def showpython(request: Request):
    res = Response()
    res.content_type = 'text/plain'
    res.charset = 'gb2312'
    res.body = 'Hello there. Sunshine boys and beautiful girls.'
    return res


# 拦截器举例
@Application.register_preinterceptor
def showheaders(ctx: Context, request: Request):
    print(request.path)
    print(request.user_agent)
    return request


@py.register_preinterceptor
def showprefix(ctx: Context, request: Request):
    print('prefix = {}'.format(ctx.router.prefix))
    return request


if __name__ == '__mian__':
    ip = '127.0.0.1'
    port = 9999
    server = make_server(ip, port, Application())
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
        server.server_close()
