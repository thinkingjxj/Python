from wsgiref.simple_server import make_server


# 返回网页的例子
def application(environ, start_response):
    status = '200 Ok'
    headers = [('Content-Type', 'text/html; charset=utf-8')]
    start_response(status, headers)
    # id=5&name=wayne
    qstr = environ.get('QUERY_STRING')
    print(qstr)
    if qstr:
        for pair in qstr.split('&'):
            k, _, v = pair.partition('=')
            print('k={}, v={}'.format(k, v))
    # 返回可迭代对象
    html = '<h2>马哥教育欢迎你</h2>'.encode()
    return [html]

ip = '127.0.0.1'
port = 9999
server = make_server(ip, port, application)
server.serve_forever()

# simple_server只是参考用，不能用于生产
