# 对类的实例属性name、age进行数据校验
# 思路：
# 1. 写函数，在__init__中先检查，如果不合格直接抛异常
# 2. 装饰器，使用inspect模块完成
# 3. 描述器

# 写函数检查
import inspect


class Typed:  # 数据描述器
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def __get__(self, instance, owner):
        if instance is not None:
            return instance.__dict__[self.name]
        return self

    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise TypeError
        instance.__dict__[self.name] = value


def typeassert(cls):
    params = inspect.signature(cls).parameters  # 顺序字典
    print(params)
    for name, param in params.items():
        print(param.name, param.annotation)
        if param.annotation != param.empty:  # 注入类属性
            setattr(cls, name, Typed(name, param.annotation))
    return cls


@typeassert
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        return '{} is {}'.format(self.name, self.age)


p = Person('tom', 20)
# p1 = Person('tom', '21')
print(p)
