
class StaticMethod:    # 非数据描述器
    def __init__(self, fn):
        self.fn = fn

    def __get__(self, instance, owner):
        return self.fn

class A:
    @StaticMethod
    def stmtd():
        print('static method')

A.stmtd()
A().stmtd()

from functools import partial

class ClassMethod:            # 非数据描述器

    def __init__(self, fn):
        self.fn = fn

    def __get__(self, instance, cls):
        #return self.fn(cls)           # 返回的是一个值，值不可调用
        return partial(self.fn, cls)   # 返回的是一个函数，而函数可以调用



class A:
    @ClassMethod
    def clsmtd(cls):    # clsmtd = ClassMethod(clsmtd)
        print(cls.__name__)


A.clsmtd
A.clsmtd()    # 未用partial函数时候：A.clsmtd(cls)()   TypeError: 'NoneType' object is not callable



