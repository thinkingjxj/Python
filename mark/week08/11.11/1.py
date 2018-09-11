# 把实例的属性保护起来，不让外部直接访问，外部使用getter读取属性和setter方法设置属性

# class Person:
#     def __init__(self, name, age=18):
#         self.name = name
#         self.__age = age
#
#     def age(self):
#         return self.__age
#     def set_age(self,age):
#         self.__age = age

# 等价写法
class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.__age = age
    @property     # 实例的属性
    def age(self):
        return self.__age
    @age.setter   # 实例的属性
    def age(self,age):
        self.__age = age
    @age.deleter   # 实例的属性
    def age(self):
        # del self.__age
        print('del')
tom = Person('Tom')
print(tom.age)
print(tom.__dict__)
print(Person.__dict__)


# 等价写法
class Person:
    def __init__(self,name,age=18):
        self.name =name
        self.__age =age
    def getage(self):
        return self.__age
    def setage(self,age):
        self.__age = age
    def delage(self):
        # del self.age
        print('del age')
    age = property(getage,setage,delage,'age property')

tom = Person('Tom')
print(tom.age)
tom.age = 20
print(tom.age)
del tom.age
