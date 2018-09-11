# 描述器：用到3个魔术方法：__get__()、__set__()、__delete__()
# object.__get__(self, instance, owner)
# object.__set__(self, instance, value)
# object.__delete__(self, instance)
# self:当前实例，调用者
# instance是owner的实例
# owner是属性的所属的类

# class A:
#     def __init__(self):
#         self.a1 = 'a1'
#         print('A.init')
#
# class B:
#     x = A()
#
#     def __init__(self):
#         print('B.init')
#
# print('-'*25)
# print(B.x)
# print(B.x.a1)
#
# print('='*25)
# b = B()
# print(b.x.a1)   # B.init  a1

# 如果在A中实现了__get__方法，看看变化

class A:
    def __init__(self):
        self.a = 'a'
        print('A.init')

    def __get__(self, instance, owner):
        print('A.__get__ {} {} {}'.format(self, instance, owner))
        return self
class B:
    x = A()

    def __init__(self):
        print('B.init')
        self.b = A()     # 实例属性也指向一个A的实例


print('%'*25)
print(1, B.x)
print(2, B.x.a)  # 如果__get__方法没有return语句或者return None会抛异常：'NoneType' object has no attribute 'a'
b = B()
print(3, b.x)
print(b.x.a)
print(b.b)      # 只有类属性是类的实例才行
# 因为定义了__get__方法，类A就是一个描述器，对类B或者类B的实例的x属性读取，成为
# 对类A的实例的访问，就会调用__get__方法
# 如何解决上例中访问报错问题，问题应该来自__get__方法。

# Python中，一个类实现了__get__、__set__、__delete__三个方法中的任何一个方法，就是描述器
# 如果仅实现了__get__，就是非数据描述器non-data descriptor
# 同时实现了__get__、__set__就是数据描述器data-descriptor
# 如果一个类的类属性设置为描述器，那么它被称为owner属主

# 属性的访问顺序
# 为上例中的类B增加实例属性x
class A:
    def __init__(self):
        self.a = 'a'
        print('A.init')

    def __get__(self, instance, owner):
        print('A.__get__ {} {} {}'.format(self, instance, owner))
        return self

class B:
    x = A()
    def __init__(self):
        print('B.init')
        self.x = 'b.x'   # 增加实例属性x

print('$'*26)
print(B.x)
print(B.x.a)
b = B()
print(b.x)
#print(b.x.a)   # AttributeError: 'str' object has no attribute 'a'
# b.x访问到了实例的属性，而不是描述器
# 继续修改代码，为类A增加__set__方法


class A:
    def __init__(self):
        self.a = 'a'
        print('A.init')

    def __get__(self, instance, owner):
        print('A.__get__ {} {} {}'.format(self, instance, owner))
        return self

    def __set__(self, instance, value):
        print('A.__set__ {} {} {}'.format(self, instance, value))
        self.data = value


class B:
    x = A()

    def __init__(self):
        print('B.init')
        #self.x = 'b.x'   # 增加实例属性x

print(B.x)
print(B.x.a)
b = B()
print(b.x)
print(b.x.a)  # 返回a，访问到了描述器数据
print(b.__dict__)
print(B.__dict__)
# 尝试增加代码，看看字典的变化
b.x = 500   # 调用数据描述器的__set__方法，或者调用非数据描述器的实例覆盖
B.x = 600   # 赋值即定义，覆盖类属性
print(b.__dict__)
print(B.__dict__)
print(A.__dict__)
