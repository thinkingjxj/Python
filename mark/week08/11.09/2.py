# 类可以继承、定制和扩展超类已有的代码
class Person:
    def lastname(self): pass
    def giveraise(self): pass
    def __str__(self): pass

class Manager(Person):              # inherit
    def giveraise(self,):pass       # customize
    def somethingelse(self,): pass  # extend

tom = Manager()
tom.lastname()
tom.giveraise()
tom.somethingelse()
print(tom)
