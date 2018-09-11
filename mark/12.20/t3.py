import socketserver
import threading


class MyHandlerServer(socketserver.BaseRequestHandler):
    def setup(self):
        super().setup()
        self.event = threading.Event()

    def handle(self):
        super().handle()
        print(self.server, self.client_address, self.request)
        while not self.event.is_set():
            data = self.request.recv(1024)
            msg = '{}'.format(data.decode()).encode()
            print(data.decode())
            self.request.send(msg)

    def finish(self):
        super().finish()
        self.event.set()

addr = ('127.0.0.1', 8080)
server = socketserver.ThreadingTCPServer(addr, MyHandlerServer)

server.serve_forever()   # 永久连接
server.shutdown()

server.server_close()   # 调用关闭套接字之前，要调用shutdown()方法，等待停止server_forever()
