from wsgiref.simple_server import make_server
from webob import Response, Request
from webob.dec import wsgify


def index(request: Request):
    res = Response()
    res.status_code = '200 ok'
    res.content_type = 'text/html'
    res.charset = 'utf-8'
    res.body = '</h1>Welcome to my world, have fun.</h1>'
    return res


def showpython(request: Request):
    res = Response()
    res.content_type = 'text/plain'
    res.charset = 'gb2312'
    res.body = '<h1>Hello there.</h1>'
    return res


def notfound(request: Request):
    res = Response()
    res.status_code = 404
    res.body = '<h1>您访问的页面被外星人劫持了</h1>'.encode('utf-8')
    return res


routable = {
    '/': index,
    '/python': showpython
}


@wsgify
def app(request: Request):
    print(request.path)
    print(request.method)
    print(request.query_string)
    print(request.GET)
    print(request.POST)
    print(request.params)
    return routable.get(request.path, notfound)(request)


if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 9999
    server = make_server(ip, port, app)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
        server.server_close()
