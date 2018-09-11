from wsgiref.simple_server import make_server
import webob


def application(environ, start_response):
    # 响应处理
    res = webob.Response(environ)
    print(res.status)
    print(res.headerlist)
    start_response(res.status, res.headerlist)

    # 请求处理
    request = webob.Request(environ)
    print(request.method)
    print(request.path)
    print(request.query_string)
    print(request.GET)
    print(request.POST)
    print('params = {}'.format(request.params))
    html = '<h2>I\'m thinking, welcome to join my world.</h2>'.encode('utf-8')
    return [html]

ip = '127.0.0.1'
port = 9999
server = make_server(ip, port, application)
server.serve_forever()





