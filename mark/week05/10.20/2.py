import inspect
from functools import wraps

# 函数参数类型检查：
# 函数参数的检查，一定是在函数外
# 函数应该作为参数，传入到检查函数中
# 检查函数拿到函数传入的实际参数，与形参声明对比
# __annotations__属性是一个字典，其中包括返回值类型的声明，假设要做
#  位置参数的判断，无法和字典中的声明对应。 使用inspect模块
# inspect模块：提供获取对象信息的函数，可以检查函数和类、类型检查
# signature()获取函数签名（包括函数名、它的参数类型、它的所在的类和名称空间及其他信息）
def logger(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        sig = inspect.signature(fn)
        params = sig.parameters        # 有序字典
        params_list = list(params)
        # 位置参数处理
        for i,v in enumerate(args):
            k = params_list[i]
            if isinstance(v, params[k].annotation):
                print(v, 'is', params[k].annotation)
            else:
                print(v, 'is not', params[k].annotation)
        # 关键字参数处理
        for k, v in kwargs.items():
            if isinstance(v, params[k].annotation):
                print(v, 'is', params[k].annotation)
            else:
                print(v, 'is not', params[k].annotation)
        return fn(*args, **kwargs)
    return wrapper

@logger
def add(x, y):
    return x + y

print(add(4, 5))