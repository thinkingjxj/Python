class A:
    def __init__(self):
        self.a = 'a'
        print('A.init')

    def __get__(self, instance, owner):  # 类A有了__get__方法，就变成了描述器，对B类或者B的实例的x属性读取，成为对类A实例的访问，就会调用__get__方法
        print('A.__get__ {} {} {}'.format(self, instance, owner))
        # 没有return语句，默认返回值为None
        return self  # 解决了返回值为None的问题

    def __set__(self, instance, value):
        print('A.__set__ {} {} {}'.format(self, instance, value))
        self.data = value

class B:
    x = A()

    def __init__(self):
        print('B.init')
        #self.b = A()    # 实例属性也指向一个A的实例
        self.x = 'b.x'  # 增加实例属性x

# # print(B.x.a)  # A.init-->a
# # b = B()
# # print(b.x.a)  # A.init-->B.init-->a
# print(B.x)   # A.init-->A.__get__ <__main__.A object at 0x000001BBE161D048> None <class '__main__.B'>-->None
# # print(B.x.a)   # AttributeError: 'NoneType' object has no attribute 'a'
# b = B()
# print(b.x)  # B.init-->A.__get__ <__main__.A object at 0x0000025EAEEDD048> <__main__.B object at 0x0000025EAF0697F0> <class '__main__.B'>-->None
# print(b.x.a)  # __get__方法中没有return语句：AttributeError: 'NoneType' object has no attribute 'a'
# print(1, b.b)  # 未触发A的__get__方法
# print(2, b.x)
print(B.x)
print(B.x.a)
b = B()
print(b.x)
#print(b.x.a)
#b.x = 300
B.x = 600
b.x = 700  # 这里调用数据描述器的__set__方法，或调用非数据描述器的实例覆盖
B.x = 500  # 赋值即定义，这是覆盖类属性
print(b.__dict__)
print(B.__dict__)



