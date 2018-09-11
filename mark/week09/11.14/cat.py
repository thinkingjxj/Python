import animal
from animal import Animal


class Cat(Animal):
    x = 'cat'
    y = 'abcd'


class Dog(Animal):
    def __dir__(self):
        return ['dog']  # 必须返回列表

print('~~~~~~~~~~~~')
print("Current Module's names = {}".format(dir()))  # 模块名词空间内的属性
print("animal Module's names = {}".format(dir(animal)))  # 指定模块名词空间内的属性
print("object's __dict__ = {}".format(sorted(object.__dict__.keys())))
print("Animal's dir() = {}".format(dir(animal)))
print("Cat's dir() = {}".format(dir(Cat)))
print("Dog's dir() = {}".format(dir(Dog)))
print('~~~~~~~~~~')
tom = Cat('tome')
print(dir(tom))
print(1, sorted(dir(tom)))  # 实例tom的属性、Cat类及索引祖先类的类属性
print(2, sorted(tom.__dir__()))  # 同上
# dir()的等价，近似如下，__dict__字典中几乎包括了所有属性
print(3, sorted(set(tom.__dict__.keys() | set(Cat.__dict__.keys()) | set(object.__dict__.keys()))))
print("Dog's dir = {}".format(dir(Dog)))
dog = Dog('snoppy')
print(dir(dog))
print(dog.__dict__)
