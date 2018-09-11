import threading
import logging
import time
logging.basicConfig(level=logging.INFO)

cups = []
event = threading.Event()


def boss(e: threading.Event):
    e.wait()
    logging.info("Good job")


def worker(n, e: threading.Event):
    while True:
        time.sleep(0.5)
        cups.append(1)
        logging.info('make 1')
        if len(cups) >= n:
            logging.info("I finished my job. {} cups.".format(len(cups)))
            e.set()
            break

b = threading.Thread(target=boss, name='boss', args=(event,))
b1 = threading.Thread(target=boss, name='boss', args=(event,))
w = threading.Thread(target=worker, name='worker', args=(10, event))
w.start()

b.start()
b1.start()
