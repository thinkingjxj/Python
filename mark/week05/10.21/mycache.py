import inspect
import functools
from functools import wraps

def logger(fn):
    local_cache = {}    #不同函数名是不同的cache
    @wraps(fn)
    def wrapper(*args, **kwargs):
        # 参数处理，构建key
        sig = inspect.signature(fn)        #匿名函数
        params = sig.parameters            # 有序字典
        params_name = [key for key in params.keys()]
        params_dict = {}          # 用意：把args，kwargs都收集到此字典中，作为缓存存放
        # 位置参数处理
        for i,v in enumerate(args):
            k = params_name[i]
            params_dict[k] = v
        # 关键字参数处理
        # for k,v in kwargs.items():
        #     params_dict[k] = v
        params_dict.update(kwargs)
        # 缺省值处理
        for k, v in params.items():
            if k not in params_dict.keys():
                params_dict[k] = v.default

        key = tuple(sorted(params_dict.items()))
        # 判断是否需要缓存
        if key not in local_cache.keys():
            local_cache[key] = fn(*args, **kwargs)

        # ret = fn(*args, **kwargs)
        return key, local_cache[key]
    return wrapper

@logger
def add(x, z, y =6):
    return x + y + z

result = []
result.append(add(4, 5))
result.append(add(4, z=5))
result.append(add(4, y=6, z=5))
result.append(add(y=6, z=5, x=4))
result.append(add(4, 5, 6))

for x in result:
    print(x)


# 过期功能：
# 一般缓存系统都有过期功能：过期是什么？
# 它是一个key过期，可以对每一个key单独设置过期时间，也可以对这些key同意设定过期时间
# 本次的实现就简单点，统一设定key的过期时间，当key生存超过了这个时间，就自动被清除
# 注意，这里并没有考虑多线程等问题，而且这种过期机制，每一次都有遍历所有数据，大量
# 数据的时候，遍历可能有效率问题
# 在上面的装饰器中增加一个参数，需要用到了带参装饰器
# 带参装饰等于在原来的装饰器外面在嵌套一层
# 清除机制，何时清除过期key？
# 用到某个key之前，先判断是否过期，如果过期重新调用函数生成新的key对应的value值
# 一个线程负责清除过期的key，这个以后实现，本次创建key之前，青醋所有过期的key

