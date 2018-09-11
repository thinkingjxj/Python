from wsgiref.simple_server import make_server
from webob import Request, Response
from webob.dec import wsgify


@wsgify
def app(request: Request)->Response:
    print(request.method)
    print(request.path)
    print(request.GET)
    print(request.POST)
    print(request.query_string)
    print('params = {}'.format(request.params))

    res = Response()
    if request.path == '/':
        res.status_code = 200
        res.content_type = 'text/html'
        res.charset = 'utf-8'
        res.body = '<h1>Hello there, welcome.</h1>'
    elif request.path == '/python':
        res.content_type = 'text/plain'
        res.charset = 'gb2312'
        res.text = 'welcome to my world'
    else:
        res.status_code = 404
        res.body = '<h1>您访问的页面被外星人劫持了</h1>'.encode('utf-8')
    return res

if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 9999
    server = make_server(ip, port, app)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
        server.server_close()





