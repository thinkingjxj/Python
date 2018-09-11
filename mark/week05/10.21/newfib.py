import functools

@functools.lru_cache()
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print([fib(x) for x in range(15)])

# lru_cache()装饰器应用：
# 同样的函数参数一定得到同样的结果
# 函数执行时间很长，且要多次执行
# 本质时函数调用的参数 => 返回值
# 缺点：不支持缓存过期，key无法过期、失效，不支持清除操作，不支持分布式，是一个单机的缓存
# 适用场景：单机上需要空间换时间的地方，可以缓存将计算变成快速查询


