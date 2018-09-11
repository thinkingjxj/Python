import inspect
import datetime
from functools import wraps
import time

def mage_cache(duration):
    def _cache(fn):
        local_dict = {}
        @wraps(fn)
        def wrapper(*args, **kwargs):
            # 清除过期的key
            def clear_expire(cache):
                lst = []
                for k, (_, stamp) in cache.items():
                    now = datetime.datetime.now().timestamp()
                    if now - stamp > duration:
                        lst.append(cache[k])
                for k in lst:
                    cache.pop(k)
            clear_expire(local_dict)
            def make_key():
                # 参数处理，构建key
                sig = inspect.signature(fn)
                params = sig.parameters
                params_list = list(params.keys())
                params_dict = {}

                #位置参数处理
                for i, v in enumerate(args):
                    k = params_list[i]
                    params_dict[k] = v
                # 关键字参数处理
                params_dict.update(kwargs)

                #缺省值处理
                for k,v in params.items():
                    if k not in params_dict:
                        params_dict[k] = v.default
                return tuple(sorted(params_dict.keys()))
            key = make_key()
            # 判断是否需要缓存（加个时间戳）

            if key not in local_dict.keys():
                local_dict[key] = (fn(*args, **kwargs),datetime.datetime.now().timestamp())
            return key, local_dict[key]

        return wrapper
    return _cache


def logger(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        ret = fn(*args, **kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        return ret
    return wrapper

@logger
@mage_cache(3)
def add(x, y, z= 5):
    time.sleep(3)
    return x + y + z

result = []
result.append(add(3, 5))
result.append(add(x=3, y=5))
result.append(add(3, 5, 6))

for x in result:
    print(x)