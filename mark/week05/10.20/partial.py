import functools

def add(x, y) -> int:
    return x + y

newadd = functools.partial(add, y = 5)

print(newadd(7))
print(newadd(7, y = 6))
print(newadd(y = 10, x = 6))

import inspect

print(inspect.signature(add))
print(inspect.signature(newadd))