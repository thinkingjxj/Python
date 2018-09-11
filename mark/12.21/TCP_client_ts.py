# 创建socket对象
# 连接到远端服务器的ip和port，connect()方法
# 传输数据：send、recv方法
# 关闭连接、释放资源

import socket
import threading
import logging
logging.basicConfig(level=logging.INFO, format='%(threadName)s %(message)s')


class ChatClientTcp:
    def __init__(self, ip='127.0.0.1', port=9090):
        self.sock = socket.socket()
        self.addr = (ip, port)
        self.event = threading.Event()

    def start(self):
        self.sock.connect(self.addr)
        threading.Thread(target=self.send).start()

    def recv(self):   # 从服务器接收数据
            while not self.event.is_set():
                try:
                    data = self.recv(1024)
                except Exception as e:
                    logging.error(e)  # 有任何异常，保证退出
                    break

    def send(self):    # 向服务器发送数据
        self.sock.send(b'hello there')

    def stop(self):
        self.sock.close()
        self.event.wait(3)
        self.event.set()
        logging.info('client stops')

def show_thread(e:threading.Event):
    while not e.wait(3):
        logging.info(threading.enumerate())

def main():
    e = threading.Event()
    cc = ChatClientTcp()
    cc.start()
    while True:
        cmd = input('>>>').strip()
        if cmd == 'quit':
            cc.stop()
            break
        cc.send(cmd)

if __name__ == '__main__':
    main()



