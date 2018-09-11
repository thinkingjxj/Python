class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastname(self):
        return self.name.split()[-1]
    def giveraise(self,percent):
        self.pay = int(self.pay*(1+percent))
    def __str__(self):
        return '[Person:%s, %s]' % (self.name, self.pay)

# # bad way
# class Manager(Person):  # inherit Person attrs
#     def giveraise(self, percent, bonus=.10):   # redefine to customize
#         self.pay = int(self.pay*(1+(percent+bonus)))
# # Manager的giveraise代码内部的self.giveraise()可能会循环--由于self已经是一个manager，self.giveraise()
# # 将会再次解析为manager.giveraise，以此类推，直到可用内存耗尽

# good way
class Manager(Person):
    def giveraise(self, percent, bonus=.10):
        Person.giveraise(self, percent + bonus)

#
# if __name__ == '__main__':
#     bob = Person('Bob Smith')
#     sue = Person('Sue Jones', job='writer', pay=10000)
#     print(bob.name, bob.pay)
#     print(sue.name, sue.pay)
#     print(bob.lastname(), sue.lastname())
#     sue.giveraise(.10)
#     print(sue.pay)
#     print(sue)
if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='writer', pay=10000)
    tom = Person('tom')
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print(bob.lastname(), sue.lastname())
    sue.giveraise(.10)
    print(sue.pay)
    print(sue)
    tom = Manager('Tom Jones', 'mgr', 50000)
    tom.giveraise(.10)
    print(tom.lastname())
    print('---All three---')
    for object in (bob, sue, tom):
        object.giveraise(.10)
        print(object)













