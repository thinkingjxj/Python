import socket
import threading
import logging
logging.basicConfig(level=logging.INFO, format='%(threadName)s %(message)s')


class ChatUdpServer:
    def __init__(self, ip='127.0.0.1', port=8080):
        self.sock = socket.socket(type=socket.SOCK_DGRAM)
        self.addr = (ip, port)
        self.event = threading.Event()
        self.clients = set()

    def start(self):
        self.sock.bind(self.addr)
        threading.Thread(target=self._recv, name='recvfrom').start()

    def _recv(self):
        # 分发？发给谁？谁给我发过我就记录谁，就认为其是客户端，就发给谁
        while not self.event.is_set():
            data, ad = self.sock.recvfrom(self.addr)
            msg = 'rcv {} {}'.format(data.decode(), ad)
            data = data.decode().strip()
            if data == 'quit':
                self.clients.remove(ad)
                continue

            self.clients.add(ad)
            # 不知道哪个客户端已经关闭了
            for c in self.clients:
                self.sock.sendto(msg.encode(), c)

            # threading.Thread(target=self.sendto, name='sendto').start()

    def stop(self):
        self.sock.close()
        self.event.set()

cs = ChatUdpServer()
cs.start()
