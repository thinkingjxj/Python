from wsgiref.simple_server import make_server
from webob import Response, Request, exc
from webob.dec import wsgify
import re


class Router:
    def __init__(self, prefix: str = ''):
        self.__prefix = prefix.rstrip('/\\')  # 前缀，例如/product
        self.__routable = []  # 三元组

    def route(self, pattern, *methods):
        def wrapper(handler):
            self.__routable.append((methods, re.compile(pattern), handler))
            return handler

        return wrapper

    def get(self, pattern):
        return self.route(pattern, 'GET')

    def post(self, pattern):
        return self.route(pattern, 'POST')

    def head(self, pattern):
        return self.route(pattern, 'HEAD')

    def match(self, request: Request):
        # 前缀处理，prefix是一级的
        if not request.path.startswith(self.__prefix):
            return
        for methods, pattern, handler in self.__routable:
            if not methods or request.method.upper() in methods:
                # not methods表示一个方法都没有定义，就让其支持全部方法
                matcher = pattern.match(request.path.replace(self.__prefix, '', 1))
                if matcher:
                    # 动态增加属性，为request增加了args、kwargs属性，在handler中使用的时候，
                    # 就可以直接从属性中，将args、kwargs拿出来就可以直接使用了
                    request.args = matcher.group()
                    request.kwargs = matcher.groupdict()
                    return handler(request)
        # 匹配不上返回None


class Application:
    Routables = []  # 前缀开头的所有Router对象

    @classmethod
    def register(cls, router: Router):
        cls.Routables.append(router)

    @wsgify
    def __call__(self, request: Request):
        for router in self.Routables:
            response = router.match(request)
            if response:
                return response
        raise exc.HTTPNotFound('您访问的页面被外星人劫走了')

# 创建Router实例
idx = Router()
py = Router('/python')

# 一定要注册
Application.register(idx)
Application.register(py)


@idx.get('^/$')   # 只匹配根
def index(request: Request):
    res = Response()
    res.status_code = 200
    res.content_type = 'text/html'
    res.charset = 'utf-8'
    res.text = '<h1>Welcome to my world.</h1>'
    return res


@py.route('/(\w+)')   # 支持所有方法，匹配/python/xxx
def showpython(request: Request):
    res = Response()
    res.content_type = 'text/plain'
    res.charset = 'gb2312'
    res.text = 'Hello there. Nice to meet you. Sunshine boys and beautiful girls.'
    return res


if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 9999
    server = make_server(ip, port, Application())
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
        server.server_close()


