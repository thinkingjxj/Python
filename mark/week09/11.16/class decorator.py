import datetime
import time
from functools import wraps


def logger(fn):
    @wraps(fn)  # wraps(fn)(wrapper)  文档字符
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        ret = fn(*args, **kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        print('decorator {} took {}'.format(fn.__name__, delta))
        return ret

    return wrapper


@logger
def add(x, y):  # add = logger(add)
    """This is a function of add."""
    time.sleep(2)
    return x + y


print(add(3, 5))


# print(add.__doc____)

# 上下文实现
# 类装饰器
class TimeIt:
    def __init__(self, fn):
        self._fn = fn
        wraps(fn)(self)  # fn：wrapper, self:wrapped
        # self.__doc__ = fn.__doc__
        # self.__name__ = fn.__name__

    def __enter__(self):
        self.start = datetime.datetime.now()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.delta = (datetime.datetime.now() - self.start).total_seconds()
        print('{} took {}s.'.format(self._fn.__name__, self.delta))
        pass

    def __call__(self, *args, **kwargs):  # 可调用
        self.start = datetime.datetime.now()
        ret = self._fn(*args, **kwargs)
        self.delta = (datetime.datetime.now() - self.start).total_seconds()
        print('{} took {}s. call'.format(self._fn.__name__, self.delta))
        return ret


@TimeIt
def add(x, y):
    """This is an add function."""
    time.sleep(1)
    return x + y


add(2, 7)
print(add.__doc__)
print(add.__name__)


# with TimeIt(add) as foo:
#     #add(4, 5)
#     foo(4, 5)
#
# print(foo(4, 6))

# 上下文应用场景
# 1.增强功能：在代码执行的前后增加代码，以增强其功能。类似装饰器的功能。
# 2.资源管理：打开了资源需要关闭，例如文件对象、网络连接、数据库连接等
# 3.权限验证：在执行代码之前，做权限的验证，在__enter__中处理
