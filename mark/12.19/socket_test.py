import socket
import threading
import logging
logging.basicConfig(level=logging.INFO, format='%(threadName)s %(message)s')


class ChatServer:
    def __init__(self, addr='127.0.0.1', port=8080):
        self.sock = socket.socket()
        self.addr = (addr, port)

        self.clients = {}    # 客户端
        self.event = threading.Event()

    def start(self):
        self.sock.bind(self.addr)
        self.sock.listen()
        threading.Thread(target=self.accept).start()

    def accept(self):                 # 多人连接
        while not self.event.is_set():
            conn, ad = self.sock.accept()   # 阻塞
            f = conn.makefile(mode='rw')
            self.clients[ad] = f         # 添加到客户端字典
            threading.Thread(target=self.recv, args=(conn, ad)).start()

    def recv(self, f, ad):   # 接收客户端数据
        while not self.event.is_set():
            try:
                data = f.readline()   # 阻塞到换行符，致命弱点
            except Exception as e:
                logging.error(e)     # 有任何异常保证退出
                data = 'quit'

            msg = data.decode().strip()
            # logging.info(data)
            # 客户端退出命令
            if msg == 'q':
                self.clients.pop(ad)
                f.close()
                logging.info('{} quits'.format(ad))

                break
            for s in self.clients.values():
                s.writelines(msg)
                s.flush()

    def stop(self):     # 停止服务
        for s in self.clients.values():
            s.close()
        self.sock.close()
        self.event.wait(3)
        self.event.set()

cs = ChatServer()
cs.start()

e = threading.Event()
while not e.wait(1):
    cmd = input('>>>').strip()
    if cmd == 'q':              # 服务端退出
        cs.stop()
        e.wait(3)
        break


