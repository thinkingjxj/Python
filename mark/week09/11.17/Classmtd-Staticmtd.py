from functools import partial


# staticmethod是非数据描述器，classmethod也是非数据描述器

# 类似staticmethod装饰器
class StaticMethod:
    def __init__(self, fn):
        self._fn = fn

    def __get__(self, instance, owner):
        # print(self, instance, owner)
        return self._fn


# 类似classmethod装饰器
class ClassMethod:
    def __init__(self, fn):
        self._fn = fn

    def __get__(self, instance, cls):
        return partial(self._fn, cls)


class A:
    @StaticMethod
    def stmtd():
        print('static method')

    @ClassMethod
    def clsmtd(cls):
        print(cls.__name__)


A.stmtd()  # static method
A().stmtd()  # static method
print(A.__dict__)
print(A.clsmtd)  # functools.partial(<function A.clsmtd at 0x000001C5E4A8C7B8>, <class '__main__.A'>)
A.clsmtd()  # A
