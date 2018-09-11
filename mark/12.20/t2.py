import threading
import socket
import logging
logging.basicConfig(level=logging.INFO, format='%(threadName)s %(message)s')


class ChatClientUdp:
    def __init__(self, ip='127.0.0.1', port=8080):
        self.sock = socket.socket()
        self.addr = (ip, port)
        self.event = threading.Event()

    def start(self):
        threading.Thread(target=self.send).start()

    def _recv(self):
        while not self.event.is_set():
            data, ad = self.sock.recvfrom(1024)
            print(data, ad)

    def send(self, data='quit'):
        self.sock.sendto(data, self.addr)

    def stop(self):
        self.sock.close()
        self.event.set()

cc = ChatClientUdp()
cc.start()



