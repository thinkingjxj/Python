import threading
import logging
import time


FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)

def boss(event: threading.Event):
    logging.info("I'm boss, waiting for U.")
    event.wait()
    logging.info("Good job")


def worker(event: threading.Event, count = 10):
    logging.info("I'm working for the boss.")
    cups = []
    while True:
        logging.info("make cups one by one")
        time.sleep(0.5)
        cups.append(1)
        if len(cups) >= count:
            event.set()
            break
    logging.info("I finished my job, Cups={}".format(len(cups)))

e = threading.Event()
W = threading.Thread(target=worker, args=(e,))
b = threading.Thread(target=boss, args=(e,))
W.start()
b.start()
