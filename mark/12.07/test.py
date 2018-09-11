
class A:
    def __init__(self, x: int):
        self.x = x

    def __add__(self, other):
        try:
            res = self.x + other.x
        except:
            try:
                o = int(other)
            except:
                o = 0
        return self.x + o

    def __iadd__(self, other):
        return self.x + other.x

    def __radd__(self, other):
        return self + other           # self.__add__(other)

a = A(3)
print(a + 1)
print(1 + a)
print(3 + a)




