import threading
import logging
from concurrent import futures
import time

FORMAT = '%(asctime)s %(processName)s %(threadName)s %(process)d:%(thread)d %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)


def worker(n):
    logging.info('begin to work {}.'.format(n))
    time.sleep(5)
    logging.info('finished {}'.format(n))

if __name__ == '__main__':
    # 创建线程池，池的容量为3
    executor = futures.ThreadPoolExecutor(max_workers=3)  # 多进程
    fs = []
    for i in range(3):
        f = executor.submit(worker, i)   # 返回Future对象，提交工作
        fs.append(f)

    # for i in range(3, 6):
    #     f = executor.submit(worker, i)    # 返回Future对象
    #     fs.append(f)

    while True:
        time.sleep(2)
        # logging.info(threading.enumerate())
        flag = True
        for f in fs:
            logging.info(f.done())
            flag = flag and f.done()
        if flag:
            executor.shutdown()  # 清理池，除非不用，不用频繁清理池
            logging.info(threading.enumerate())  # 多进程是看线程已经没必要了
            break




