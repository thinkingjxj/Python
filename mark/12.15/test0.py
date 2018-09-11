import threading
import time
import logging

FORMAT = "%(asctime)s %(threadName)s %(thread)s %(message)s"
logging.basicConfig(level=logging.INFO)

cups = []


def worker(count=10):
    logging.info("I'm working for u.")
    flag = False
    while True:
        if len(cups) >= count:
            flag = True
        time.sleep(0.001)
        if not flag:
            cups.append(1)
        if flag:
            break
    logging.info("{} finished. cups = {}".format(threading.current_thread().name, len(cups)))


for _ in range(10):
    threading.Thread(target=worker, args=(1000,)).start()

