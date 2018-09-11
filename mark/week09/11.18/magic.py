# 反射相关的魔术方法
# __getattr__()、__setattr__()、__delattr__()这三个魔术方法，分别测试

class Base:
    n = 0

class Point(Base):
    z = 6
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

    def __getattr__(self, item):      # 按照继承关系找不到，才会执行此方法，如果没有此方法，会抛异常
        return 'Missing {}'.format(item)

p = Point(4, 5)
print(p.x)         # 4
print(p.z)         # 6
print(p.__dict__)  # {'x': 4, 'y': 5}
print(p.n)         # 0
print(p.t)         # missing
# 一个类的属性会按照继承关系找，如果找不到，就会执行__getattr__()方法，如果没有此方法，就会抛出AttributeError异常表示找不到属性
# 查找属性的顺序：instance.dict->instance.class.dict->继承的祖先类（直到object）的dict->调用getattr()
print('~~~~~~~~~~~~~~~~')

# __setattr__()
class Base:
    n = 0


class Point(Base):
    z = 6

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

    def __getattr__(self, item):
        return 'Missing {}'.format(item)

    def __setattr__(self, key, value):
        print('setattr {}={}'.format(key, value))
        # self.__dict__[key] = value

p = Point(3, 9)
print(1, p.x)      # Missing，实例的属性被__setattr__()拦截了
print(2, p.z)      # 6
print(3, p.n)      # 0
print(4, p.t)      # Missing
print(p.__dict__)   # {}空字典，被__setattr__()拦截了
# 实例的属性被__setattr__()拦截了
# 实例通过.点设置属性，如同self.x=x，就会调用__setattr__(),属性要加到实例的__dict__中，就需要自己完成

print(Point.__dict__)

# __setattr__()方法，可以拦截对实例属性的增加、修改操作，如果要设置生效，需要自己操作实例的__dict__
# __delattr__()


class Point:
    Z = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __delattr__(self, item):
        print('Can not del {}'.format(item))

p = Point(12, 5)
del p.x             # 未被删除
p.z = 15
del p.z             # 未被删除
del p.Z             # 未被删除
print(p.__dict__)   # {'y': 5, 'z': 15, 'x': 12}
print(Point.__dict__)
del Point.Z            # 被删除了
print(Point.__dict__)
# __delattr__()可以阻止通过实例删除属性的操作，但是通过类依然可以删除类的属性

# __getattribute__


class Base:
    n = 0


class Point(Base):
    z = 6

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getattr__(self, item):
        return 'missing {}'.format(item)

    def __getattribute__(self, item):
        return item    # 如果return self.item则会出错：RecursionError: maximum recursion depth exceeded while calling a Python object
        # raise Exception

p = Point(1, 7)
print(p.__dict__)   # __dict__
print(p.x)          # x
print(p.z)          # z
print(p.n)          # n
print(p.t)          # t
print(Point.__dict__)
print(Point.z)      # 6
# 实例的所有属性访问，第一个都会调用__getattribute__方法，它阻止了属性的查找，该方法应该返回（计算后的）值或者抛一个AttributeError异常
# 它的return值将作为属性查找的结果，如果抛错Attribute异常，则会直接调用__getattr__方法，因为表示属性没有找到

class Point(Base):
    z = 6
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getattr__(self, item):
        return 'missing {}'.format(item)

    def __getattribute__(self, item):
        #raise AssertionError('Not Found')
        #return self.__dict__[item]
        return object.__getattribute__(self, item)

p = Point(3, 6)
print(p.__dict__)       # {'y': 6, 'x': 3}
print(p.x)              # 3
print(p.y)              # 6
print(p.z)              # 6
print(p.t)              # missing t
print(Point.__dict__)
print(Point.z)          # 6

# __getattribute__方法中为了避免在该方法中无限递归，它的实现应该永远调用基类的同名方法以访问需要的任何属性，例如object.getattribute(self, name)
# 注意，除非你明确知道__getattribute__方法用来做什么，否则不要使用它

# __getattr__()：当通过搜索实例、实例的类及祖先类查不到属性，就会调用此方法
# __setattr__()：通过.访问实例属性，进行增加、修改都要调用它
# __delattr__()：当通过实例来删除属性时调用此方法
# __getattribute__：实例的所有属性都从这个方法开始
# 实例属性查找顺序：
# __getattribute__()-->instance.__dict__-->instance.__class__.__dict__-->
# 继承的祖先类（直到object）的__dict__-->调用__getattr__()


