# 装饰器（无参）
# 它是一个函数，函数作为它的形参，返回值也是一个函数，可以使用@functionname方式，简化调用
# 装饰器也是高阶函数，但装饰器是对传入函数的功能的装饰（功能增强）

# Documentation Strings 文档字符串：在函数语句块的第一行，且习惯是多行文本，所以使用三引号
# 惯例是首字母大写，第一行写概述，空一行，第三行写详细描述
# 可以使用特殊属性__doc__访问这个文档

from functools import wraps

def logger(fn):                  # 日志
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print('begin')               # 增强功能
        ret = fn(*args, **kwargs)
        print('end')                 # 增强功能
        return ret
    return wrapper

@logger
def add(x, y):
    return x + y

print(add(12, 5))


# 完整版(日志)

import datetime
from functools import wraps
import time

def logger(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        '''
        This is a wrapper
        '''
        # before 功能增强
        start = datetime.datetime.now()
        ret = fn(*args, **kwargs)
        # after 功能增强
        delta = (datetime.datetime.now() - start).total_seconds()
        print(delta)
        return ret
    return wrapper

@logger
def add(x, y):
    '''
    This is a function of addition

    : x: int
    : y: int
    : return: int
    '''
    time.sleep(3)
    return x + y

print(add(12, 6))
print(add.__name__, add.__doc__)


# 带参装饰器：是一个函数，函数作为它的形参，返回值是一个不带参的装饰器函数
# 使用@functionname(参数列表) 方式调用
# 可以看作在装饰器外层又加了一层函数

def logger(duration):   #获取函数的执行时长，对时长超过阈值的函数记录一下
    def _logger(fn):
        @wraps(fn)            # 带参装饰器
        def wrapper(*args, **kwargs):
            start = datetime.datetime.now()
            ret = fn(*args, **kwargs)
            delta = (datetime.datetime.now() - start).total_seconds()
            print('so slow') if delta > duration else print('so fast')
            return ret
        return wrapper
    return _logger

# 将记录功能提取出来，这样就可以通过外部提供的函数来灵活的控制输出

def logger(duration, func = lambda name,duration: print('{} took {s}'.format(name, duration))):
    def _logger(fn):
        def wrapper(*args, **kwargs):
            start = datetime.datetime.now()
            ret = fn(*args, **kwargs)
            delta = (datetime.datetime.now() - start).total_seconds()
            if delta > duration:
                func(fn.__name__, duration)
            return ret
        return wrapper   # return functools.update_wrapper(wrapper, fn)
    return _logger