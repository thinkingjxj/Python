__author__ = 'thinking'

import datetime
import time

def copy_properities(src):
    def _copy(dst):
        dst.__name__ = src.__name__
        dst.__name__ = src.__doc__
        return dst
    return _copy

def logger(duration, func = lambda name,duration: print('{} took {}s'.format(name,duration))):
    def _logger(fn):
        @copy_properities(fn)
        def wrapper(*args,**kwargs):
            start = datetime.datetime.now()
            x = fn(*args,**kwargs)
            delta = (datetime.datetime.now() - start).total_seconds()
            if delta > duration:
                func(fn.__name__,duration)
            return x
        return wrapper
    return _logger

@logger
def add(x,y):
    return x + y


print(add(15,3))
