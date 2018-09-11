import pymysql
from queue import Queue
import threading
import logging
import time

FORMAT = "%(asctime)s %(thread)s %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


class ConnPool:
    def __init__(self, size, *args, **kwargs):
        if not isinstance(size, int) or size < 1:
            size = 8
        self._pool = Queue(size)
        for i in range(size):
            self._pool.put(pymysql.connect(*args, **kwargs))
        self.local = threading.local()

    def get_conn(self):
        return self._pool.get()  # 阻塞

    def return_conn(self, conn):
        self._pool.put(conn)

    def __enter__(self):
        if getattr(self.local, 'conn', None) is None:  # self.local.conn=None
            # getattr(x, 'y') is equivalent to x.y
            self.local.conn = self.get_conn()
        return self.local.conn.cursor()  # 返回一个游标

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.local.conn.roolback()
        else:
            self.local.conn.commit()
        self.return_conn(self.local.conn)
        self.local.conn = None


pool = ConnPool(4, '192.168.86.100', 'root', '123456', 'test')


def foo(pool: ConnPool):
    with pool as cursor:  # 自动拿连接并归还，还自动提交或回滚
        with cursor:
            sql = 'select * from reg'
            cursor.execute(sql)
            # print(cursor.fetchone())
            sql = 'show processlist'  # 观察连接，权限小只能看自己的
            cursor.execute(sql)
            for x in cursor:  # 查看源码知cursor是一个生成器
                conn = pool.local.conn
                logging.info("{} {}".format(x, conn._sock.getsockname()))
    time.sleep(5)


for i in range(8):
    t = threading.Thread(target=foo, args=(pool,))
    t.start()
