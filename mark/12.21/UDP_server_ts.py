import socket
import threading
import logging
logging.basicConfig(level=logging.INFO, format='%(threadName)s %(message)s')


class ChatServerUdp:
    def __init__(self, ip='127.0.0.1', port=9999):
        self.sock = socket.socket(type=socket.SOCK_DGRAM)
        self.addr = (ip, port)
        self.event = threading.Event()
        self.s = set()      # 客户端集合

    def start(self):
        self.sock.bind(self.addr)
        threading.Thread(target=self.recv, name='recv').start()

    def recv(self):
        while not self.event.is_set():
            data, ad = self.sock.recvfrom(1024)   # from client
            data = data.decode()
            self.s.add(ad)
            if data.strip() == 'quit':
                self.s.remove(ad)
                continue
            msg = '{} {}\n{}\n'.format(data, *ad)
            logging.info(msg)
            for c in self.s:     # send the msg to every client
                self.sock.sendto(msg.encode(), c)

    def stop(self):
        for c in self.s:
            self.sock.sendto(b'End', c)
        self.sock.close()
        self.event.set()

if __name__ == '__main__':
    cs = ChatServerUdp()
    cs.start()
    threading.Event().wait(3)


