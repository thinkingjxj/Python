class Person:
    def __init__(self, name, age=18):
        self.name = name
        self._age = age

    def _getname(self):
        return self.name

    def __getage(self):
        return self._age


tom = Person('Tom')
print(tom._getname())
#print(tom.__getage())   # 没有此属性
print(tom.__dict__)
print(tom.__class__.__dict__)
print(tom._Person__getage())
