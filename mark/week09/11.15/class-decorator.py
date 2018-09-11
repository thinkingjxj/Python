import time
import datetime
from functools import wraps


class TimeIt:
    def __init__(self, fn):
        self._fn = fn
        wraps(fn)(self)      # doc文档复制

    def __enter__(self):
        self.start = datetime.datetime.now()
        print(self.start)
        return self

    def __call__(self, *args, **kwargs):
        print('__call__')
        start = datetime.datetime.now()
        ret = self._fn(*args, **kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        print('decorator {} took {}'.format(self._fn.__name__, delta))
        return ret

    def __exit__(self, exc_type, exc_val, exc_tb):     # 里面的参数有异常时候才用
        delta = (datetime.datetime.now() - self.start).total_seconds()
        print('content {} took {}'.format(self._fn.__name__, delta))
        return


# def logger(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         start = datetime.datetime.now()
#         ret = fn(*args, **kwargs)
#         delta = (datetime.datetime.now() - start).total_seconds()
#         return ret
#     return wrapper

@TimeIt
def add(x, y):      # add = TimeIt(add)
    """This is a function of add."""
    time.sleep(2)
    return x + y


# with TimeIt(add) as f:
#     print(add(4, 5))
#     print(f(2, 3))

print(add(3, 6))
print(add.__doc__)



