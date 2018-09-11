from wsgiref.simple_server import make_server
from webob import Response, Request, exc
from webob.dec import wsgify
import re


class DictObj:
    def __init__(self, d: dict):
        if isinstance(d, (dict,)):
            self.__dict__['_dict'] = d
        else:
            self.__dict__['_dict'] = {}

    def __getattr__(self, item):
        try:
            return self._dict[item]
        except KeyError:
            raise AttributeError('Attribute {} not found.'.format(item))

    def __setattr__(self, key, value):
        # 不允许设置属性
        raise NotImplementedError


class Router:
    def __init__(self, prefix=''):
        self.__prefix = prefix.rstrip('/\\')
        self.routetable = []

    def __route(self, pattern, *methods):
        def wrapper(handler):
            self.routetable.append((methods, re.compile(pattern), handler))
            return handler
        return wrapper

    def get(self, pattern):
        return self.__route(self, pattern, 'GET')

    def post(self, pattern):
        return self.__route(self, pattern, 'POST')

    def head(self, pattern):
        return self.__route(self, pattern, 'HEAD')

    def match(self, request: Request)->Response:
        # 前缀处理
        if not request.path.startswith(self.__prefix):
            return
        for methods, pattern, handler in self.routetable:
            if not methods or request.method.upper() in methods:
                matcher = pattern.match(request.path.replace(self.__prefix, '', 1))
                if matcher:
                    request.args = matcher.group()
                    request.kwargs = DictObj(matcher.groupdict())  # 命名分组组成的字典
                    return handler(request)
        # 匹配不上返回None


class Application:
    # 动态修改路由配置
    ROUTERS = []  # 匹配有序的路径
    GET = 'GET'
    # 注册函数
    @classmethod
    def register(cls, router: Router)->Response:
        cls.ROUTERS.append(router)

    @wsgify
    def __call__(self, request: Request)->Response:
            for methods, pattern, handler in self.ROUTERS:
                # not methods 表示一个方法没提供，就默认支持所有方法
                if not methods or request.method.upper() in methods:
                    if pattern.match(request.path):
                        return handler(request)
            raise exc.HTTPNotFound('您访问的页面被外星人劫持了')


idx = Router()
py = Router('/python')

Application.register(idx)
Application.register(py)


@idx.get('/')
def index(request: Request):     # index = Application.register('/')(index)
    res = Response()
    res.status_code = 200
    res.content_type = 'text/html'
    res.charset = 'utf-8'
    res.body = '<h1>Nice to meet you, you are so beautiful.</h1>'.encode('utf-8')
    return res


@py.get('/python')
def showpython(request: Request):
    res = Response()
    res.content_type = 'text/plain'
    res.charset = 'gb2312'
    res.body = 'Hi, sunshine boys and beautiful girls'.encode('utf-8')
    return res


# # 注册
# Application.register('/', index)
# Application.register('/python', showpython)

if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 9999
    server = make_server(ip, port, Application())
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
        server.server_close()


