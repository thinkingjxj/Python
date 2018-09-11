import threading
import socket
import logging
logging.basicConfig(level=logging.INFO, format='%(threadName)s %(message)s')


class ChatClientUdp:
    def __init__(self, ip='127.0.0.1', port=9999):
        self.sock = socket.socket(type=socket.SOCK_DGRAM)
        self.addr = (ip, port)
        self.event = threading.Event()

    def send(self, msg: str):
        message = 'msg = {}, {}:{} '.format(msg, *self.addr)
        self.sock.sendto(message.encode(), self.addr)

    def recv(self):
        while not self.event.is_set():
            data, ad = self.sock.recvfrom(1024)
            logging.info('recv {} from {}'.format(data, ad))

    def stop(self):
        self.sock.close()
        self.event.wait(2)
        self.event.set()


cc = ChatClientUdp()
while True:
    cmd = input('>>').strip()
    if cmd == 'quit':
        cc.stop()
        break
    cc.send(cmd)
logging.info('End')


