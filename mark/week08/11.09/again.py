# 属性装饰器：把实例的属性保护起来，不让外部直接访问，外部使用getter读取属性和setter方法设置属性
class Person:
    def __init__(self, name, age=18):    # 可以给默认值也可以不给，不给实例化的时候要有相应的位置参数，给的话实例化时候也给就会覆盖此默认值
        self.name = name
        self.__age = age
    def age(self):
        return self.__age
    def set_age(self, age):   # 外部给的age值可以修改相当于重新设置age值
        self.__age = age
tom = Person('tom')
print(tom.age())
tom.set_age(20)
print(tom.age())
# 有没有更简单的方式呢？
class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.__age = age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        self.__age = age
    @age.deleter
    def age(self):
        # del self.__age
        print('del')
tom = Person('Tom')
print(tom.age)
tom.age = 25
print(tom.age)
# def tom.age

# property装饰器：后面跟的函数名就是以后的属性名。它就是getter，这个必须有，有了它至少是只读属性
# setter装饰器：与属性名同名，且接收2个参数，第一个是self，第二个是将要赋值的值。有了它，属性可写
# deleter装饰器：可以控制是否删除属性，很少用
# property装饰器必须在前，setter、deleter装饰器在后
# property装饰器能通过简单的方式，把对方法的操作变成对属性的访问，并起到了一定隐藏效果
# 其他写法

class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.__age = age
    def getage(self):
        return self.__age
    def setage(self, age):
        self.__age = age
    def delage(self):
        # del self.__age
        print('del age')
    age = property(getage, setage, delage, 'age property')

tom = Person('Tom')
print(tom.age)
tom.age = 28
print(tom.age)

# 还可以如下
class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.__age = age
    age = property(lambda self:self.__age)
tom = Person('Tom')
print(1, tom.age)
tom.__age = 30
print(2, tom.age)

# 对象的销毁
# 类中可以定义__del__方法，称为析构函数（方法）
# 作用：销毁类的实例的时候调用，以释放占用的资源
# 由于python实现了垃圾回收机制，这个方法不能确定何时执行，有必要是，请使用del语句删除实例，来手动调用这个方法
class Person:
    def __init__(self, name, age = 18):
        self.name = name
        self.age = age

    def __del__(self):
        print('delete {}'.format(self.name))

tom = Person('tom')
del tom

# 封装：面向对象的三要素之一，封装encapsulation
# 将数据和操作组织到类中，即属性和方法
# 将数据隐藏起来，给使用者提供操作，使用者通过操作就可以获取或者修改数据，getter和setter
# 通过访问控制，暴露适当的数据和操作给用户，该隐藏的隐藏起来，保护成员或私有成员













