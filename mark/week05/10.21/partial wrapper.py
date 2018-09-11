# partial方法：偏函数：把函数部分的参数固定下来，相当于为部分参数添加了一个固定的默认值，形成一个新的函数并返回
# 从partial生成的新函数，是对原函数的封装
import functools

def add(x, y) ->int:
    return x + y

newadd = functools.partial(add, y=5)
print(newadd(7))
print(newadd(7, y=6))
print(newadd(y=7, x=10))

import inspect

print(inspect.signature(newadd))

def add(x, y, *args) -> int:
    print(args)
    return x + y

newadd = functools.partial(add, 1,3,5,6,7)

print(newadd())
print(newadd(9))
# print(newadd(9, 10, x=26, y=20))

print(inspect.signature(newadd))

functools._make_key((4, 6), {'z', 3}, False)