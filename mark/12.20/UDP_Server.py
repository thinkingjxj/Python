import threading
import socket
import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')


class ChatServerUdp:
    def __init__(self, ip='127.0.0.1', port=8080):
        self.sock = socket.socket()
        self.addr = (ip, port)
        self.event = threading.Event()
        self.clients = set()     # 记录一下客户端

    def start(self):
        self.sock.bind(self.addr)
        threading.Thread(target=self.rev, name='rev').start()

    def rev(self):
        while not self.event.is_set():
            data, ad = self.sock.recvfrom(1024)
            data = data.decode()
            self.clients.add(ad)
            if data.strip() == 'quit':
                self.clients.remove(ad)
                continue
            self.clients.add(ad)

            for c in self.clients:
                self.sock.sendto(data.encode(), c)   # 并不能保证对方收到，也不关心对方是否收到

    def stop(self):
        for i in self.clients:
            self.sock.sendto(b'End', i)

        self.sock.close()
        self.event.set()


if __name__ == '__main__':
    cs = ChatServerUdp()
    cs.start()
    threading.Event().wait(3)

