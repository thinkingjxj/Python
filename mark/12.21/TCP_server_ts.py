import threading
import socket
import logging
logging.basicConfig(level=logging.INFO, format='%(threadName)s %(message)s')


class ChatServerTcp:
    def __init__(self, ip='127.0.0.1', port=9090):
        self.sock = socket.socket()
        self.addr = (ip, port)
        self.event = threading.Event()
        # 放客户端的字典
        self.clients = {}

    def start(self):
        self.sock.bind(self.addr)
        self.sock.listen()
        threading.Thread(target=self.accept).start()

    def accept(self):    # 多人连接
        while not self.event.is_set():
            conn, ad = self.sock.accept()
            self.clients[ad] = conn
            logging.info('{} recv from {}'.format(conn, ad))

        threading.Thread(target=self.recv).start()

    def recv(self, sock: socket.socket, ad):   # 接收客户端数据并发送给各个客户端
        while not self.event.is_set():
            data = sock.recv(1024)
            msg = data.decode().strip()
            if msg == 'quit':
                self.clients.pop(ad)
                self.sock.close()
                break

            for s in self.clients.values():
                s.send(msg.encode())

    def stop(self):
        for s in self.clients.values():
            s.close()
        self.sock.close()
        self.event.set()

cs = ChatServerTcp()
cs.start()


