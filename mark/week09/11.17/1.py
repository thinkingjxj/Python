import contextlib
from functools import total_ordering


@contextlib.contextmanager
def foo():
    print('enter')
    try:
        yield 3, 5
    finally:
        print('exit')  # 必须做的清理工作
    # yield              # yield返回值给f了，等价于ruturn None
    print('end')


with foo() as f:
    # raise Exception
    print(f)

# contextlib.contextmanager：它是一个装饰器实现上下文管理，装饰一个函数，而不用像类一样
# 实现__enter__和__exit__方法
# 对函数的要求时必须有yield，也就是这个函数必须返回一个生成器，且只有yield一个值
