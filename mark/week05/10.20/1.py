from functools import wraps
import inspect


def logger(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        sig = inspect.signature(fn)  # 获取函数签名
        params = sig.parameters      # 有序字典
        params_list = tuple(params.keys())
        # 位置参数处理
        for i,v in enumerate(args):
            k = params_list[i]
            if isinstance(v, params[k].annotation):    # annotation参数注解
                print(v, 'is', params[k].annotation)
            else:
                pass
        # 关键字参数处理
        for k, v in kwargs.items():
            if isinstance(v, params[k].annotation):
                print('===')
        #ret = fn(*args, **kwargs)
        return fn(*args, **kwargs)
    return wrapper

@logger
def add(x, y):
    return x + y


print(add(4, 5))