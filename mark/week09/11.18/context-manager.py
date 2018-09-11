# contextlib.contextmanager:它是一个装饰器实现上下文管理，装饰一个函数，而
# 不用像类一样实现__enter__和__exit__方法，对函数的要求，必须有yield，也就是
# 这个函数必须返回一个生成器，且yield只有一个值

import contextlib


@contextlib.contextmanager
def foo():
    print('Enter')  # 相当于__enter__()
    yield  # yield的值只能有一个，作为__enter__方法的返回值
    print('Exit')  # 相当于__exit__()


with foo() as f:  # f接收yield语句的返回值
    # raise Exception()  # 此程序看似不错但是，增加一个异常，发现不能保证exit的执行，怎么办？增加try,finally
    print(f)

print('~~~~~~~~~~~~~~~~~~~~``')


@contextlib.contextmanager
def foo():
    print('Enter')
    try:
        yield
    finally:
        print('Exit')


with foo() as f:
    #raise Exception()
    print(f)

# 这么做的意义？yield为生成器函数增加了上下文管理
import contextlib
import datetime
import time

print('?????????????')
@contextlib.contextmanager
def add(x, y):  # 为生成器函数增加了上下文管理
    start = datetime.datetime.now()
    try:
        yield x + y
    finally:
        delta = (datetime.datetime.now() - start).total_seconds()
        print(delta)


with add(4, 5) as f:
    # raise Exception()
    time.sleep(2)
    print(f)

# 如果业务逻辑简单可以使用函数加装饰器方式，如果业务复杂，用类的方式加__enter__和__exit__方法方便
