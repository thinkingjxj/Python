
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
        self.x = 'b.x'    # 增加实例属性,由于__set__此时的self.x不在实例的字典而在类B的字典中
        self.y = 'b.y'


print(B.x)
print(B.x.a)

b = B()
print(1, b.x)
print(2, b.x.a)
print(b.y)
#print(3, b.y.a)  # AttributeError: 'str' object has no attribute 'a'
print(b.__dict__)
print(B.__dict__)

# 原来不是什么数据描述器优先级高，而是把实例的属性从__dict__中给去除了
# 造成了该属性如果是数据描述器优先访问的假象

# Python中的描述器应用非常广泛
# Python方法（包括staticmethod()和classmethod()都实现为非数据描述器。
# 因此，实例可以重新定义和覆盖方法。这允许单个实例获取与同一类的其他实例不同的行为

