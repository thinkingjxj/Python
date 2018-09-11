# 柯里化： 指的是将原来接受两个参数的函数变成新的接受一个参数的函数的过程。新的函数返回一个原有第二个参数为参数的函数
# Z = f(x, y) 转换成 Z = f(x)(y) 的形式

def add(x, y):
    return x + y


def add(x):
    def _add(y):
        return x + y
    return _add


print(add(5)(6))