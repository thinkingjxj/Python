import datetime
import time


def logger(duration):
    def _logger(fn):
        def wrapper(*args, **kwargs):
            start = datetime.datetime.now()
            ret = fn(*args, **kwargs)
            delta = (datetime.datetime.now() - start).total_seconds()
            print('so slow') if delta > duration else print('fast')
            return ret

        return wrapper

    return _logger


@logger(3)
def add(x, y):
    time.sleep(3)
    return x + y

print(add(3, 5))
