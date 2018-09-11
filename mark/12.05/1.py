class Property:    # 数据描述器
    def __init__(self, fget, fset=None):
        self.fget = fget
        self.fset = fset

    def __get__(self, instance, owner):
        if instance is not None:
            return self.fget(instance)
        return self

    def setter(self, fn):
        self.fset = fn
        return self         # 返回类的实例

class A:
    def __init__(self, data):
        self._data = data

    @Property      # data = Property(data) => data = obj
    def data(self):
        return self._data

    @data.setter       # data = data.setter(data) => data = obj
    def data(self, value):
        self.data = value

a = A(100)
print(a.data)     # 触发get方法
a.data = 200      # 触发set方法
print(a.data)     # 触发get方法



