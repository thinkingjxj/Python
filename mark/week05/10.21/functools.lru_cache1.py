# @functools.lru_cache(maxsize = 128, typed = False)
# least-recently-used装饰器，最近最少使用，cache：缓存
# 如果maxsize设置为None，则禁用LRU功能，并且缓存可以无限制增长。当maxsize是2的幂次时，LRU功能执行的最好
# 如果typed设置为True，则不同类型的函数参数将单独缓存。例如，f(3)和f(3.0)将被视为具有不同结果的不同调用
import functools
import time

@functools.lru_cache()
def add(x, y, z = 3):
    time.sleep(z)
    return x + y

print(add(4,5))
print(add(4.0,5))
print(add(4,5.0))
print(add(4, y=6))
print(add(x=4,y=6))
print(add(y=6, x=4))
# lru_cache装饰器：通过一个字典缓存被装饰函数的调用和返回值