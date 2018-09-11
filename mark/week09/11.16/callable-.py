# Python中一切皆对象，函数也不例外


def foo():
    print(foo.__module__, foo.__name__)


foo()  # 等价于：foo.__call__()


# 函数即对象，对象foo加上()，就是调用对象的__call__()方法
# __call__，类中有此方法，其实例就可以像函数一样调用
# 可调用对象：定义一个类，并实例化得到其实例，将实例像函数一样调用


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self, *args, **kwargs):
        return "Point({}, {})".format(self.x, self.y)


p = Point(4, 5)
print(p)  # 实例对象
print(p())  # Point(4, 5)


class Adder:
    def __call__(self, *args, **kwargs):
        ret = 0
        for x in args:
            ret += x
        self.ret = ret
        return ret


adder = Adder()
print(adder(4, 5, 6))  # 15
print(adder.ret)  # 15


# 练习：定义一个斐波那契数列的类，方便调用，计算第n项

class Fib:
    def __init__(self):
        self.items = [0, 1, 1]

    def __call__(self, n):
        if n < len(self.items):
            return self.items

        for i in range(len(self.items) - 1, n):
            self.items.append(self.items[i - 1] + self.items[i])
        return self.items[n], self.items

    def __iter__(self):
        return iter(self.items)

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


print(Fib()(10))
