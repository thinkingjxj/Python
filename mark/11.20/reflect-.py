# class Point:
#     Z = 5
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __delattr__(self, item):
#         print('Can not del {}'.format(item))  # 如果是self.item会出错：AttributeError: 'Point' object has no attribute 'item'
# # __delattr__可以阻止通过实例删除属性的操作，但是通过类依然可以删除类属性
# p = Point(4, 5)
# print(p.__dict__)
# del p.x
# p.z = 15
# print(p.__dict__)


class Base:
    n = 0


class Point(Base):
    z = 6
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getattr__(self, item):
        return 'Missint {}'.format(item)

    def __getattribute__(self, item):
        return item   # 如果返回self.item会出错RecursionError: maximum recursion depth exceeded while calling a Python object
        # return object.__getattribute__(self, item)  # 避免在该方法中无限递归，它的实现应该永远调用基类的同名方法以访问需要的任何属性
p = Point(4, 5)
print(p.__dict__)
print(p.x)       # x
print(p.y)       # y
print(p.z)       # z
print(p.t)       # t
print(p.f)       # f
print(p.n)       # n
# 实例的所有属性访问会首先调用__getattribute__方法，它阻止了属性的查找，该方法应该返回（计算后的）值或者抛异常
# 它的return值将作为属性查找的结果。如果抛异常，则会直接调用__getattr__方法，因为表示属性没有找到

