from threading import Thread, Event
import logging
logging.basicConfig(level=logging.INFO)


def do(event: Event, interval: int):
    while not event.wait(interval):
        logging.info('do sth')

e = Event()
Thread(target=do, args=(e, 3)).start()

e.wait(10)
e.set()
print('Main exit')
