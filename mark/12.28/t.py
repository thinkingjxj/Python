import pymysql
from pymysql import cursors
from queue import Queue
import threading


class ConnPool:
    def __init__(self, size, host='192.168.86.100', name='th', password=None):
        self.host = host
        self.name = name
        self.password = password
        self._size = size
        self._pool = Queue(size)
        for i in range(size):
            conn = pymysql.connect()
            self._pool.put(conn)

    def get_conn(self):
        return self._pool.get()

    def rt_conn(self, conn:pymysql.connections.Connection):
        if isinstance(conn, pymysql.connections.Connection):
            self._pool.put(conn)

    @property
    def size(self):
        return self._pool.qsize()

    def __enter__(self):
        return self.get_conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            pass
        except:
            pass
        finally:
            pool.rt_conn(conn)


# 信号量：考虑到并发问题
# queue本身就是线程安全的，多进程中的queue跨结点跨主机，用不好易出问题

pool = ConnPool(5)
conn = pool.get_conn()
print(conn)
print(pool.size)

with conn as cursor:
    with cursor:
        pass
pool.rt_conn(conn)



