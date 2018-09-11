# 上下文管理，执行顺序：初始化->进入with语句->enter语句块->with语句块中内容执行->exit语句块
import sys

class Point:
    def __init__(self):
        print('init')

    def __enter__(self):
        print('Enter')
        return self        # self赋给了f，之后with语句块中的p和f就相等了

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exit')

# 极端的例子，调用sys.exit()，它会退出当前解释器，打开python解释器，在里面敲入sys.exit()
# 窗口直接关闭了。也就是说碰到这句，Python运行环境直接退出了

p = Point()
with p as f:
    print(p == f)   # False   为什么p和f不相等？ 问题出在__enter__上，它将自己的返回值赋给f，修改返回值给f就好了
    #sys.exit()
    #raise Exception('error')  # 有了此句，后面的print语句不会执行
    print('do sth')

print('outer')
# 从运行结果来看，依然执行了__exit__函数，哪怕退出Python运行环境，说明上下文管理很安全
# __enter__方法返回值就是上下文中使用的对象，with语法会把它的返回值赋给as子句的变量

# __exit__(self, exctype, excvalue, traceback)
# 这三个参数都与异常有关，如果该上下文退出时没有异常，这3个参数都为None
# 如果有异常，参数意义如下：
# exc_type, 异常类型
# exc_value, 异常的值
# traceback, 异常的追踪信息
# __exit__方法返回一个等效True的值，则压制异常；否则，继续抛出异常

# 整理
class Point:
    def __init__(self):
        print('init')

    def __enter__(self):
        print('Enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_tb)     # traceback
        print(exc_type)   # class 'Exception
        print(exc_val)    # 异常值:New Error
        return 'abc'      # 非0返回True，否则抛异常

p = Point()
with p as f:
    raise Exception('New Error')
    print('do sth')

print('Outer')

