import socket
import selectors
import threading

selector = selectors.DefaultSelector()
clients = {}


def accept(sock):

    conn, addr = sock.accept()
    conn.setblocking(False)
    clients[addr] = conn

    selector.register(sock, selectors.EVENT_READ, recv)


def recv(conn: socket.socket):
        data = conn.recv(1024).strip().decode()

        msg = 'Your msg = {}'.format(data)
        print(msg)
        conn.send(msg.encode())


sock = socket.socket()
sock.bind(('127.0.0.1', 9999))
sock.listen()
sock.setblocking(False)
e = threading.Event()

key = selector.register(sock, selectors.EVENT_READ, accept)
print(key)


while not e.is_set():
    events = selector.select()   # 阻塞
    if events:
        print(events)      # 列表

    for key, mask in events:
        callback = key.data   # accept 或 recv
        callback(key.fileobj)









