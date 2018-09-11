from magweb import MagWeb
from wsgiref.simple_server import make_server


idx = MagWeb.Router()
py = MagWeb.Router('/python')

MagWeb.register(idx)
MagWeb.register(py)


@idx.get('^/$')  # 只匹配根
def index(request: MagWeb.Request) -> MagWeb.Response:
    res = MagWeb.Response()
    res.status_code = 200
    res.content_type = 'text/html'
    res.charset = 'utf-8'
    res.body = '<h1>Welcome to my world, please have fun.</h1>'
    return res


@py.route('/{id:int}')
def showpython(request: MagWeb.Request) -> MagWeb.Response:
    res = MagWeb.Response()
    res.content_type = 'text/plain'
    res.charset = 'utf-8'
    res.body = '<h1>Hello there, sunshine boys and beautiful girls, how are you?</h1>'
    return res




if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 9999
    server = make_server(ip, port, MagWeb())
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
