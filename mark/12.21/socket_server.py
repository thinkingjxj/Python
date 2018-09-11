import socketserver
import threading


socketserver.BaseServer
socketserver.ThreadingTCPServer
class MyRequestHandler(socketserver.BaseRequestHandler):
    def setup(self):
        super().setup()
        self.event = threading.Event()

    def handle(self):
        super().handle()
        while not self.event.is_set():
            data = self.request.recv(1024)
            self.request.send(data)

    def finish(self):
        super().finish()
        self.event.set()

server = socketserver.ThreadingTCPServer(('127.0.0.1', 9090), MyRequestHandler)

server.serve_forever()
server.shutdown()
server.server_close()




