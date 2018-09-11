# class MyClass:
#     '''A example class'''
#     x = 'abc'    # 类属性、类变量
#
#     def __init__(self):
#         print('init')
#
#     def foo(self):   # 类属性、method方法对象，不是普通的函数function了
#         return 'My Class'
#
# print(MyClass.x)
# print(MyClass.foo)
# print(MyClass.__doc__)
#
# a = MyClass()   # 实例化，会调用__init__、初始化
#
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def showage(self):
#         print('{} is {}'.format(self.name, self.age))
#
# tom = Person('Tom', 20)
# jerry = Person('Jerry', 18)
# print(tom.name, tom.age)
# print(tom.name, jerry.age)
# jerry.age += 1
# print(jerry.age)
# jerry.showage()
#
#
# class MyClass:
#     def __init__(self):
#         print('self in init = {}'.format(id(self)))
#
# c = MyClass()
# d = MyClass()
# print('c = {}'.format(id(c)))
# print('d = {}'.format(id(d)))
#
#
# class Person:
#     age = 3
#     def __init__(self, name):
#         self.name = name
#
# #tom = Person('Tom', 20)
# jerry = Person('Jerry')
# tom = Person('Tom')
# print(tom.name, tom.age)
# print(jerry.name, jerry.age)
#
# Person.age = 30
# print(Person.age)
# print(Person.age, tom.age, jerry.age)
#
# # 实例变量是每一个实例自己的变量，是自己独有的；类变量是类的变量，是类的属性和方法
#
# class Person:
#     age = 3
#
#     def __init__(self, name):
#         self.name = name
#
# print('-------class--------')
# print(Person.__class__)
# print(Person.__dict__)
#
#
# tom = Person('Tom')
# print(tom.__class__)
# print(tom.__dict__)
# print('-------tom class---------')
# print(tom.__class__.__name__)
# print(tom.__class__.__dict__.items(), end = '\n')

class Person:
    age = 3
    height = 170
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

tom = Person('Tom')
jerry = Person('Jerry', 20)
Person.age = 30
print(Person.age, tom.age, jerry.age)

print(Person.height, tom.height, jerry.height)
jerry.height += 10
print(Person.height, tom.height, jerry.height)
tom.height += 10
print(Person.height, tom.height, jerry.height)

Person.height += 15
print(Person.height, tom.height, jerry.height)
Person.weight = 70
print(Person.weight, tom.weight, jerry.weight)

print(tom.__dict__['height'])
#print(tom.__dict__['weitht'])

# 总结：是类的，也就是这个类的所有实例的，其实例都可以访问到；是实例的，就是这个实例自己的，通过类访问不到
# 类变量是属性类的变量，这个类的所以实例可以共享这个变量
# 实例可以动态的给自己增加属性，实例__dict__[变量名]和实例.变量名都可以访问到
# 实例的同名变量会隐藏这类变量，或者说是覆盖了这个类变量

# 增加类变量
def add_name(name, clz):
    clz.NAME = name     # 动态增加类属性

# 改进成装饰器
def add_name(name):
    def wraper(clz):
        clz.NAME = name
        return clz
    return wraper

@add_name('Tom')
class Person:
    AGE = 3

print(Person.NAME)
# 之所以能够装饰，本质上是为类对象动态的添加了一个属性，而Person这个标识符指向这个类对象

class Person:
    def normal_method():
        print('normal')

Person.normal_method()
# Person().normal_method()

class Person:
    @classmethod
    def class_method(cls):
        print('class = {0.__name__} ({0})'.format(cls))
        cls.HEIGHT = 70
    @staticmethod
    def static_method():
        print(Person.HEIGHT)

Person.class_method()
Person.static_method()
print(Person.__dict__)
