import animal
from animal import Animal


class Cat(Animal):
    x = 'cat'
    y = 'abcd'


class Dog(Animal):
    def __dir__(self):
        return ['dog']  # 必须返回列表


print("Current Module's names = {}".format(dir()))
print("animal Module's names = {}".format(dir(animal)))
print("object's__dict__ = {}".format(sorted(object.__dict__.keys())))  # object的字典
print("Animal's dir() = {}".format(dir(Animal)))
print("Cat's dir() = {}".format(dir(Cat)))
print('~~~~~~~~~~~~~~~~~~~~~````')
tom = Cat('Tom')
print(sorted(dir(tom)))
print(sorted(tom.__dir__()))

print(tom.__dict__.keys())
print(Cat.__dict__.keys())
print(object.__dict__.keys())
print(sorted(set(tom.__dict__.keys() | set(Cat.__dict__.keys()) | set(Object.__dict__.keys()))))
