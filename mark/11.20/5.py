# class Person:
#     def __init__(self, name:str, age:int):
#         if not self.checkdata(((name,str), (age,int))):
#             return
#         self.name = name
#         self.age = age
#     def checkdata(self, params):
#         for data, tp in params:
#             if not isinstance(data, tp):
#                 return

#
# class Typed:
#     def __init__(self, tp):
#         self.type = tp
#
#
#     def __get__(self, instance, owner):
#         pass
#
#     def __set__(self, instance, value):
#         print('T.set: ', self, instance, value)
#         if not isinstance(value, self.type):
#             raise ValueError(value)
#
#
# class Person:
#     name = Typed(str)
#     age = Typed(int)
#
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age


# p = Person('tom', 18)

import inspect


# params = inspect.signature(Person).parameters
# print(inspect.signature(Person))   # (name:str, age:int)
# print(inspect.signature(Person).parameters)
#
# for name, param in params.items():
#     #print(name, param)
#     print(name, param.annotation)  # param.annotation返回的是类型


class Typed:  # 数据描述器
    def __init__(self, tp):
        self.type = tp

    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        print('T.set: ', self, instance, value)
        if not isinstance(value, self.type):
            raise ValueError(value)


class TypeAssert:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, name, age):
        params = inspect.signature(self.cls).parameters
        print(params)
        for name, param in params.items():
            print(name, param.annotation)
            if param.annotation != param.empty:  # 注解定义过
                setattr(self.cls, name, Typed(param.annotation))


@TypeAssert
class Person:  # Person = TypeAssert(Person)
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


p = Person('tom', 18)
