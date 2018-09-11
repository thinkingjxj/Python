class Property:
    def __init__(self):
        pass

    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        pass

    def setter(self):
        pass

    def getter(self):
        pass

    def deleter(self):
        pass

    def __getattribute__(self, item):
        pass

    def __delete__(self, instance):
        pass


class A:
    def __init__(self, data):
        self._data = data

    @Property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value


