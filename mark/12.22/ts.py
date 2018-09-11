import socketserver
import threading


class ChatHandler(socketserver.BaseRequestHandler):
    def setup(self):
        super().setup()
        self.event = threading.Event()
        self.clients = []
        self.request = self.clients[self.client_address]

    def handle(self):
        super().handle()
        while not self.event.is_set():
            data = self.request.recv(1024).strip().decode()
            if data == 'quit':
                break
            for c in self.clients:
                c.send(data.encode())


    def finish(self):
        super().finish()






