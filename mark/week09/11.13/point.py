
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


a = Point(1, 3)
b = Point(2, 4)

print(a == b)

s = (a, b)
print(s)

# 列表为什么不可哈希：__hash__ = None
# 源码中有一句__hash__=None，也就是如果调用__hash__()相当于None()，一定会报错
# 所有类都继承自object，而这个类是具有__hash__()方法的，如果一个类不能被hash，就是把__hash__设置为None了
print(hash(None))
