import socket
import threading
import datetime
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(thread)s %(message)s')


class ChatServer:
    def __init__(self, ip='127.0.0.1', port=6666):    # 启动服务
        self.sock = socket.socket()
        self.addr = (ip, port)
        self.clients = {}         # 客户端

    def start(self):      # 启动监听
        self.sock.bind(self.addr)   # 绑定
        self.sock.listen()          # 监听
        # accept会阻塞主线程，所以开一个新线程
        threading.Thread(target=self._accept).start()

    def _accept(self):    # 多人连接，也就是多个客户端连接
        conn, client = self.sock.accept()   # 阻塞
        self.clients[client] = conn         # 添加到客户端字典中
        # 准备接收数据，recv是阻塞的，开启新的线程
        threading.Thread(target=self._recive, args=(conn, client)).start()

    def _recive(self):        # 接收客户端数据
        while True:
            data = self.sock.recv(1024)  # 阻塞到数据到来
            msg = "{:%Y/%m/%d %H:%M:%S} {}:{}".format(datetime.datetime.now(), client, data.decode())
            logging.info(msg)
            for s in self.clients.values():
                s.send(msg)

    def stop(self):          # 停止服务
        for s in self.clients.values():
            s.close()
        self.sock.close()


cs = ChatServer()
cs.start()







