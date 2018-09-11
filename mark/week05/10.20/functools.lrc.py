# @functools.lru_cache(maxsize = 128, typed = False)
# least-recently-used装饰器。最近最少使用，cache缓存
# 如果maxsize设置为None,则禁用LRU功能，并且缓存可以无限制增长。
# 当maxsize是2的幂时，LRU功能执行得最好
# 如果typed设置为True，则不同类型得函数参数将单独缓存。
# 例如，f(3)和f(3.0)将被视为具有不同结果得不同调用

import functools

@functools.lru_cache()
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print([fib(x) for x in range(30)])
