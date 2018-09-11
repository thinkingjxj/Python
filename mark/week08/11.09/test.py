class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastname(self):
        return self.name.split()[-1]
    def giveraise(self, percent):
        self.pay = int(self.pay*(1 + percent))
    def __str__(self):
        return '[Person:%s, %s]' % (self.name, self.pay)


if __name__ == '__mian__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=10000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print(bob.lastname(), sue.lastname())
    sue.giveraise(.10)
    print(sue.pay)
    print(sue)

