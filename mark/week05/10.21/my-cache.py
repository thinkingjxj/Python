import inspect
import datetime
from functools import wraps
import time

def mage_cache(duration):
    def _cache(fn):
        local_cache = {}
        @wraps(fn)
        def wrapper(*args, **kwargs):
            #清除过期的key
            expire_keys = []
            for k, (_, stamp) in local_cache.items():
                now = datetime.datetime.now().timestamp()
                if now - stamp > duration:
                    expire_keys.append(k)
            for k in expire_keys:
                local_cache.pop(k)

            # 参数处理，构建key
            sig = inspect.signature(fn)
            params = sig.parameters    # 有序字典
            params_list = list(params.keys())
            params_dict = {}
            #位置参数处理
            for i, v in enumerate(args):
                k = params_list[i]
                params_dict[k] = v
            #关键字参数处理
            params_dict.update(kwargs)
            # 缺省值处理
            for k, v in params.items():
                if k not in params_dict.keys():
                    params_dict[k] = v.default
            #判断是否需要缓存
            key = tuple(sorted(params_dict.keys()))
            if key not in local_cache.keys():
                local_cache[key] = (fn(*args, **kwargs), datetime.datetime.now().timestamp())
            return key, local_cache[key]
        return wrapper
    return _cache

def logger(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        ret = fn(*args, **kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        print(fn.__name__, delta)
        return ret
    return wrapper

@logger
@mage_cache(3)
def add(x, y, z=5):
    time.sleep(3)
    return x + y + z

result = []
result.append(add(4, 5))
#result.append(add(4, z=5))
result.append(add(4, y=6, z=5))
result.append(add(y=6, z=5, x=4))
result.append(add(4, 5, 6))

for x in result:
    print(x)
