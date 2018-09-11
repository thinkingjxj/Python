# 创建Socket对象
# 连接到远端服务端的ip和port，connect()方法
# 传输数据：send、recv方法发送接收数据
# 关闭连接、释放资源
import threading
import socket
import logging
logging.basicConfig(level=logging.INFO, format='%(threadName)s %(message)s')


class ChatClient:
    """群聊客户端"""
    def __init__(self, ip='127.0.0.1', port=8080):
        self.sock = socket.socket()
        self.addr = (ip, port)
        self.event = threading.Event()

    def start(self):
        self.sock.connect(self.addr)   # 连到服务器
        threading.Thread(target=self.recv, name='recv').start()

    def recv(self):
        while True:
            try:
                data = self.sock.recv()
            except Exception as e:
                logging.info(e)
                break
            logging.info(data)

    def send(self, data='quit'):
        self.sock.send(data)

    def stop(self):
        self.sock.close()
        self.event.wait(3)
        self.event.set()


def main():
    c = ChatClient()
    c.start()          # 启动连接，建立sock与服务器的连接

    e = threading.Event()

    while True:
        cmd = input('>>>').strip()
        if cmd == 'quit':
            c.send()
            c.stop()
            break
        c.send(cmd)

if __name__ == '__main__':
    main()




