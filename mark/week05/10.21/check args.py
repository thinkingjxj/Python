# 业务功能：测试形参和实参是否一致

import inspect
from functools import wraps

def check(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        sig = inspect.signature(fn)
        params = sig.parameters       # 有序字典
        lst = list(params)         # 转换成字典
        # 位置参数是否一致
        for i, v in enumerate(args):
            k = lst[i]
            if isinstance(v, params[k].annotation):
                print(v, 'is', params[k].annotation)
            else:
                print(v, 'is not', params[k].annotation)
        # 关键字参数是否一致
        for k, v in kwargs.items():
            if isinstance(v, params[k].annotation):
                print(v, 'is', params[k].annotation)
            else:
                print(v, 'is not', params[k].annotation)
        return fn(*args, **kwargs)
    return wrapper


@check
def add(x, y: int = 7) -> int:
    return x + y

print(add(5, 8))