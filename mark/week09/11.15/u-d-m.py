class Point:
    def __init__(self):
        print('init')

    def __enter__(self):  # 进去了帮忙做事情
        print(self.__class__)
        return self               # 返回值给了f

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.__class__.__name__)   # 退出帮忙做事情

p = Point()

# import sys

with Point() as f:
    # sys.exit()
    print(f == p)
    print(f is p)
    print(f)
    print(p)



# sys.exit()  # 之后任何语句都不执行，但with语句中的内容会执行