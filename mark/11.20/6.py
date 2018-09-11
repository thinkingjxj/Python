# 类似classmethod装饰器
from functools import partial


class ClassMethod:
    def __init__(self, fn):
        self._fn = fn

    def __get__(self, instance, cls):
        ret = partial(self._fn, cls)
        return ret


class A:
    @ClassMethod            # clsmtd = Classmethod(clsmtd)
    def clsmtd(cls):
        print(cls.__name__)


print(A.__dict__)
print(A.clsmtd)       # functools.partial(<function A.clsmtd at 0x0000023E81E9B620>, <class '__main__.A'>)
A.clsmtd()            # A
# partial函数，固定某些参数，返回新函数