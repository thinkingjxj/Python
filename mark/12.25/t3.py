from wsgiref.simple_server import make_server, demo_app
import cgi
from urllib import parse
import webob


def application(environ, start_response):
    status = '200 ok'
    headers = [('Content-Type', 'text/html;charset=utf-8')]
    start_response(status, headers)

    request = webob.Request(environ)
    print(request.method)
    print(request.query_string)  # 查询字符串
    print(request.path)          # 路径
    print(request.GET)           # GET方法的所有数据
    print(request.POST)          # POST方法的所以数据
    print('params = {}'.format(request.params))  # 所有数据、参数

    qstr = environ.get('QUERY_STRING')
    print(qstr)
    print(cgi.parse_qs(qstr))   # 过期了
    print(parse.parse_qs(qstr))   # 字典
    print(parse.parse_qsl(qstr))   # 二元组列表
    html = '<h1>马哥教育欢迎你</h1>'.encode('utf-8')
    return [html]

ip = '127.0.0.1'
port = 9999
server = make_server(ip, port, application)    # 返回一个新的server
server.serve_forever()

# simple_server只是参考用，不能用于生产





# def make_server(
#     host, port, app, server_class=WSGIServer, handler_class=WSGIRequestHandler
# ):
#     """Create a new WSGI server listening on `host` and `port` for `app`"""
#     server = server_class((host, port), handler_class)
#     server.set_app(app)
#     return server


