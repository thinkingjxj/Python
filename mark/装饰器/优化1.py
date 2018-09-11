__author__ = 'thinking'
import datetime,time,functools

def logger(t1,t2):
    def _logger(fn):
        def wrapper(*args,**kwargs):
            #'''This is a wrapper'''
            print('before')
            start = datetime.datetime.now()
            x = fn(*args,**kwargs)
            duration = (datetime.datetime.now() - start).total_seconds()
            if duration > t1 and duration < t2:
                print('function {} took {}s'.format(fn.__name__,duration))
            print('after')
            return x
        return wrapper
    return _logger

@logger(3,5)
def add(x,y):
    #'''
   # This is a function
    #return int
    #x int
    #y int
    #'''
    print('call add')
    time.sleep(3)
    ret = x + y
    return ret

print(add(4,12))