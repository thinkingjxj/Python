# class Animal:
#     def shout(self):
#         print('Animal shout')
#
# a = Animal()
# a.shout()
#
# class Cat:
#     def shout(self):
#         print('Cat shout')
#
# c = Cat()
# c.shout()
# # 以上两个类是独立的，无关联


#


# 继承：可以让子类从父类获取特征（属性和方法）
# 父类：也成基类、超类
# 子类：也成派生类


# class Animal:
#     def __init__(self, name):
#         self._name = name
#
#     def shout(self):
#         print('{} shout'.format(self.__class__.__name__))
#
#     @property
#     def name(self):
#         return self._name
#
#
# a = Animal('monster')
# a.shout()
# print(a.name)
#
#
# class Cat(Animal):
#     pass
#
#
# cat = Cat('garfield')
# cat.shout()
# print(cat.name)
#
#
# class Dog(Animal):
#     pass
#
#
# dog = Dog('ahuang')
# dog.shout()
# print(dog.name)

# class Animal:
#     __count = 0
#     height = 0
#
#     def __init__(self, age, weight, height):
#         self.age = age
#         self.height = height
#         self.__count += 1
#         self.__weight = weight
#
#     def eat(self):
#         print('{} eat'.format(self.__class__.__name__))
#
#     def __getweight(self):
#         print(self.__weight)
#
#     @classmethod
#     def shoutcount1(cls):
#         print(cls.__count)
#
#     @classmethod
#     def __shoutcount2(cls):
#         print(cls.__count)
#
#
# class Cat(Animal):
#     name = 'CAT'
#
#
# ca = Cat(10, 30, 40)
# ca.eat()
# print(ca.height)
# ca.shoutcount1()
#
# a = Animal(10, 15, 18)
# a.shoutcount1()
# a.eat()
# print(Animal.__dict__)
# print(ca.__dict__)
# print(super.__dict__)
# print(super().__dict__)  # 运行结果跟第96行一样

# class Animal:
#     def shout(self):
#         print('Animal shout')
#
#
# class Cat(Animal):
#     # 覆盖了父类的方法
#     def shout(self):
#         print('miao')
#
#     # 覆盖了自身的方法，显式调用了父类的方法
#     def shout(self):
#         print(super())
#         print(super(Cat, self))
#         super().shout()
#         super(Cat, self).shout()  # 等价于super()
#         self.__class__.__base__.shout(self)  # 不推荐
#
#
# a = Animal()
# a.shout()
# c = Cat()
# c.shout()
# print(a.__dict__)
# print(c.__dict__)
# print(Animal.__dict__)
# print(Cat.__dict__)
#
#
# # 类方法和静态方法
# class Animal:
#     @classmethod
#     def class_method(cls):
#         print('class_method_animal')
#
#     @staticmethod
#     def statci_method():
#         print('static_method_animal')
#
#
# class Cat(Animal):
#     @classmethod
#     def class_method(cls):
#         print('class_method_cat')
#
#     @staticmethod
#     def statci_method():
#         print('static_method_cat')
#
#
# c = Cat()
# c.class_method()
# c.statci_method()
#
#
# # 这些方法都可以覆盖，原理都一样，属性字典的搜索顺序
#
# # 继承中的初始化
# class A:
#     def __init__(self, a):
#         self.a = a
#
#
# class B(A):
#     def __init__(self, b, c):
#         self.b = b
#         self.c = c
#
#     def printv(self):
#         print(self.b)
#         # print(self.a)
#
#
# f = B(200, 300)
# print(f.__dict__)
# print(f.__class__.__bases__)
# f.printv()
#
#
# class A:
#     def __init__(self):
#         self.a1 = 'a1'
#         self.__a2 = 'a2'
#         print('A init')
#
#
# class B(A):
#     pass
#
#
# b = B()
# print(b.__dict__)
#
# b = B()
# print(b.__dict__)
#
#
# # B实例的初始化会自动调用基类A的__init__方法
#
# class B(A):
#     def __init__(self):
#         self.b1 = 'b1'
#         print('B init')
#         A.__init__(self)
#
#
# b = B()
# print(b.__dict__)
#
#
# # 如何正确的初始化？
# class Animal:
#     def __init__(self, age):
#         print('Animal init')
#         self.age = age
#
#     def show(self):
#         print(self.age)
# #
# #
# # class Cat(Animal):
# #     def __init__(self, age, weight):
# #         print('Cat init')
# #         self.age = age + 1
# #         self.weight = weight
# #
# #
# # c = Cat(10, 5)
# # c.show()
#
#
# class Cat(Animal):
#     def __init__(self,age,weight):
#         # 调用父类的__init__方法的顺序决定着show方法的结果
#         super().__init__(age)
#         print('Cat init')
#         self.age = age + 1
#         self.weight = weight
#         #super().__init__(age)
#
# c = Cat(10,5)
# c.show()

class Animal:
    def __init__(self,age):
        print('Animal init')
        self.__age = age
    def show(self):
        print(self.__age)
class Cat(Animal):
    def __init__(self,age,weight):
        super().__init__(age)
        print('Cat init')
        self.__age = age + 1
        self.__weight = weight

c = Cat(10,5)
c.show()   # Animal init, 10, Cat init, 11,最终10被11覆盖了
print(c.__dict__)
print(Animal.__dict__)




