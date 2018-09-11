import datetime
import time


def copy_pro(src):
    def _copy(dst):
        dst.__name__ = src.__name__
        dst.__doc__ = src.__doc__
        return dst

    return _copy


def logger(duration):
    def _logger(fn):
        @copy_pro(fn)
        def wrapper(*args, **kwargs):
            '''This is a wrapper'''
            start = datetime.datetime.now()
            x = fn(*args, **kwargs)
            delta = (datetime.datetime.now() - start).total_seconds()
            print('so slow') if delta > duration else print('so fast')
            return x

        return wrapper

    return _logger


@logger(5)
def add(x, y):
    '''This is a function'''
    time.sleep(3)
    return x + y


print(add(5, 6))
print(add.__name__, add.__doc__, sep='\n')
