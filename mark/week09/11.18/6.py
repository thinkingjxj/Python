# 实现非数据描述器:仿造staticmethod，实现Staticmethod装饰器功能
# 实现非数据描述器：仿造classmethod，实现Classmethod装饰器功能

from functools import partial

class Staticmethod:
    def __init__(self, fn):
        self.fn = fn

    def __get__(self, instance, owner):
        return self.fn


class A:
    @Staticmethod    # f = Staticmethod(f)
    def stmtd():
        print('static method')

A.stmtd()
A().stmtd()

# 类classmethod装饰器
class Classmethod:
    def __init__(self, f):
        self.f = f

    def __get__(self, instance, owner):
        ret = self.f(owner)
        return ret

class A:
    @Classmethod   # clsmtd = Classmethod(clsmtd)
    def clsmtd(cls):
        print(cls.__name__)

print(A.__dict__)
A.clsmtd
#A.clsmtd()  # TypeError: 'NoneType' object is not callable
# A.clsmtd() <=> A.clsmtd(cls)()
# A.clsmtd = A.clsmtd(cls)
# 应该用partial函数

from functools import partial

class ClassMthod:
    def __init__(self, fn):
        self._fn = fn

    def __get__(self, instance, cls):  # 把原来的owner修改为类cls
        ret = partial(self._fn, cls)
        return ret

class A:
    @Classmethod
    def clsmtd(cls):
        print(cls.__name__)

print(A.__dict__)
print(A.clsmtd)
print('????????????')
A.clsmtd()
