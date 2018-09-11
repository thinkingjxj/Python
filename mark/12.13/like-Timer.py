import threading
import logging
logging.basicConfig(level=logging.INFO)
event = threading.Event()


def add(x, y):
    logging.info('add x+y={}'.format(x + y))


class Timer:
    def __init__(self, interval, fn, *args, **kwargs):
        self.interval = interval
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.event = threading.Event()

    def start(self):
        threading.Thread(target=self._do).start()

    def cancle(self):
        self.event.set()

    def _do(self):
        self.event.wait(self.interval)
        if not self.event.is_set():
            self.fn(*self.args, **self.kwargs)
        self.event.set()

t = threading.Timer(3, add, args=(4, 5))
t.start()
