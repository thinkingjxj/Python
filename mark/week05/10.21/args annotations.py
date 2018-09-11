# python是动态语言，变量可以随时被赋值，且赋值为不同的类型
# python不是静态编译语言，变量类型是在运行器决定的
# 动态语言很灵活，但这中特性也是弊端
# 难发现：由于不做任何类型检查，直到运行期间问题才显现出来，或者线上运行时才能暴露问题
# 难使用：函数的使用者看到函数的时候，并不知道你的函数设计，并不知道应该传入什么类型的数据
# 解决这种弊端：增加文档Documentation String
#   这只是一个惯例，不是强制标准，不能要求程序员一定为函数提供说明文档
#   函数定义更新了，文档未必同步更新
# function annotations 函数注解：
# 对函数的参数进行类型注解，对函数的返回值进行类型注解，只对函数参数做一个辅助的说明，并不对函数参数进行类型检查
# 提供给第三方工具，做代码分析，发现隐藏的bug
# 函数注解信息，保存在__annotations__属性中

def add(x:int, y:int) -> int:
    '''

    :param x: int
    :param y: int
    :return: int
    '''
    return x + y

# 业务应用：
# 函数参数的检查一定在函数外，函数应该作为参数，传入到检查函数中
# 检查函数拿到函数传入的实际参数，与形参声明对比
# __annotations__属性是一个字典，其中包括返回值类型的声明。
# 假设要做位置参数的判断，无法和字典中的声明对应，使用inspect模块
# inspect模块：提供获取对象信息的函数，可以检查函数和类、类型检查
# signature(callable)获取签名（函数名、它的参数类型、它所在的类和名称空间及其他信息）

import inspect

def add(x:int, y:int, *args, **kwargs) -> int:
    return x + y

sig = inspect.signature(add)    # 获取签名
print(sig)
params = sig.parameters   # 有序字典
print(params)
print('~'*30)
print(1, sig.parameters['x'])
print(sig.parameters['x'].annotation)   # 关键字为x 的注解信息
print(2, sig.parameters['y'])
print(sig.parameters['y'].annotation)
print(3, sig.parameters['args'])
print(sig.parameters['args'].annotation)
print(4, sig.parameters['kwargs'])
print(sig.parameters['kwargs'].annotation)



# inspect模块
inspect.isfunction(object)   # 是否是函数
inspect.ismethod(object)     # 是否是类方法
inspect.isgenerator(object)  # 是否是生成器对象
inspect.isgeneratorfunction(object)  # 是否是生成器函数
inspect.isclass(object)      # 是否是类
inspect.ismodule(inspect)    # 是否是模块
inspect.isbulitin(print)     # 是否是内建对象

# parameter对象，不同于parameters
# 保存在元组中，是只读的
# name,annotation,default,empty(特殊的类，用来标记default属性或注释annotation属性的空值)
# kind, 实参如何绑定到形参，就是形参的类型，包括：
#  POSITIONAL_ONLY    值必须是位置参数提供
#  POSITIONAL_OR_KEYWORD    值可以是位置参数也可以是关键字参数
#  VAR_POSITIONAL     可变位置参数
#  VAR_KEYWORD        可变关键字参
#  KEYWORD_ONLY       keyword-only参数

import inspect

def add(x, y:int = 7, *args, z, t = 10, **kwargs) -> int:
    return x + y

sig = inspect.signature(add)
print(sig)

params = sig.parameters    # 有序字典
print(params)

print(params['x'].annotation)
print(params['y'].annotation)
print(params['args'].annotation)
print(params['z'].annotation)
print(params['t'].annotation)
print(params['kwargs'].annotation)


