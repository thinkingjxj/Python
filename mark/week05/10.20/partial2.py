import functools

def add(x, y, *args) -> int:
    print(args)
    return x + y

newadd = functools.partial(add, 1, 2, 4, 7, 8)

print(newadd(7))    # 加到了args的后面
print(newadd(7,10))
print(newadd())

import inspect

print(inspect.signature(newadd))