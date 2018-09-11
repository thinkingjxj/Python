from wsgiref.simple_server import make_server
from webob import Request, Response, exc
from webob.dec import wsgify
import re


class Application:

    Routable = []

    @classmethod
    def route(cls, pattern, *methods):
        def wrapper(handler):
            cls.Routable.append((methods, re.compile(pattern), handler))
            return handler
        return wrapper

    @classmethod
    def get(cls, pattern):
        return cls.route(pattern, 'GET')

    @classmethod
    def post(cls, pattern):
        return cls.route(pattern, 'POST')

    @classmethod
    def head(cls, pattern):
        return cls.route(pattern, 'HEAD')

    @wsgify
    def __call__(self, request: Request):
        for methods, pattern, handler in self.Routable:
            # not methods表示一个方法都没有定义，即支持所有方法
            if not methods or request.method.upper() in methods:
                matcher = pattern.match(request.path)
                if matcher:
                    # 动态增加属性，为request增加了args、kwargs属性，在handler中使用的时候
                    # 就可以直接从属性中，将args、kwargs拿出来就可以直接使用了
                    request.args = matcher.group()  # 所有分组组成的元组，包括命令的
                    request.kwargs = matcher.groupdict()  # 命名分组组成的字典
                    return handler(request)
        raise exc.HTTPNotFound('<h1>您访问的页面被外星人劫持了</h1>'.encode())


@Application.get('^/$')   # index=Application.route('/')(index)
def index(request: Request):
    res = Response()
    res.status_code = 200
    res.content_type = 'text/html'
    res.charset = 'utf-8'
    res.text = '<h1>Welcome to my world</h1>'
    return res


@Application.route('^/python')   # 支持所有方法
def showpython(request: Request):
    res = Response()
    res.content_type = 'text/plain'
    res.charset = 'gb2312'
    res.body = 'Hello there, you are so beautiful'.encode()
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
