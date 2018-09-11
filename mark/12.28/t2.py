from webob.dec import wsgify
from wsgiref.simple_server import make_server
from webob import Request, Response


@wsgify
def application(request: Request):
    print(request.path)
    print(request.method)
    print(request.GET)
    print(request.POST)
    print(request.params)

    res = Response()
    if request.path == '/':
        res.charset = 'utf-8'
        res.content_type = 'text/html'
        res.status_code = '200 ok'
        res.body = '<h1>Welcome!</h1>'.encode()
    elif request.path == '/python':
        res.content_type = 'text/plain'
        res.charset = 'gb2312'
        res.body = '<h1>Hello there.</h1>'.encode()
    else:
        res.status_code = '404'
        res.body = '<h1>您访问的页面被外星人劫持了</h1>'.encode('utf-8')
    return res


if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 9999
    server = make_server(ip, port, application)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
        server.server_close()


