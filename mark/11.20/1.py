class A:
    @classmethod   # 非数据描述器
    def foo(cls):
        pass

    @staticmethod  # 非数据描述器
    def bar():
        pass

    @property      # 数据描述器
    def z(self):   # <property object at 0x000001F85ED763B8>
        return 5

    def getfoo(self):   # 非数据描述器
        return self.foo

    def __init__(self):    # 非数据描述器
        self.foo = 100
        self.bar = 200      # foo、bar都可以在实例中覆盖，但是z覆盖不了
        #self.z = 300
a = A()
print(a.__dict__)
print(A.__dict__)

