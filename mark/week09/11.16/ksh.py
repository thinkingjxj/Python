
class A:
    def __init__(self):
        self.a = 'a'
        self.b = 'b'

    def __repr__(self):
        return 'repr: {}, {}'.format(self.a, self.b)

    def __str__(self):
        return 'str: {}, {}'.format(self.a, self.b)


print(A())   # print函数使用__str__
print([A()])   # []使用__str__，但其内部使用__repr__
print([str(A())])  # str使用__str__
