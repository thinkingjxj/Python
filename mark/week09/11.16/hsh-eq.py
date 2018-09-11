from collections import Hashable


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


a = Point(4, 5)
b = Point(4, 5)
print(hash(a))
print(hash(b))   # 相等
print(a is b)    # False
print(a == b)    # True
print(set((a, b)))  # 去重
print({a, b})       # 去重
print(isinstance(a, Hashable))   # True

# __eq__，对应==操作符，判断2个对象是否相等，返回bool值
# __hash__方法只是返回一个hash值作为set的key，但是去重，还需要__eq__
# hash值相等，只是hash冲突，不能说明两个对象是相等的
# 因此，提供__hash__方法是为了作为set或者dict的key的，所以去重要同时提供__eq__方法

# list为什么不可hash？
# 源码中有一句__hash__=None，也就是如果调用__hash__()相当于None(),一定会报错
# 所有类都继承自object，而这个类是具有__hash__()方法的，如果一个类不能被hash，就是把__hash__设置为None了
