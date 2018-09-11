from functools import partial


class Property:
    def __init__(self, data):
        self.data = data

    def __get__(self, instance, owner):
        return self.data

    def __set__(self, instance, value):
        self.data = value
        #return self

    def setter(self, fn):  # real signature unknown
        self.data = fn
        return self

    def deleter(self):
        pass
    # fset = Property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


class A:
    def __init__(self, data):
        self._data = data

    @Property
    def data(self):          # data = Property(data)
        return self._data

    @data.setter
    def data(self, value):
        self._data = value



a = A(6)
print(a.data)
a.data = 200
print(a.data)

class C(object):

        def __init__(self, x):
            self._x = x
        @property
        def x(self):    # x = property(x)
            """I am the 'x' property."""
            return self._x

        @x.setter
        def x(self, value):
            self._x = value

        @x.deleter
        def x(self):
            del self._x

c = C(5)
print(c.x)
