# 运算符重载
class A:
    def __init__(self, x):
        self.x = x

    def __sub__(self, other):   # -
        return self.x - other.x

    def __isub__(self, other):  # -=
        tmp = self.x - other.x
        return tmp

    def __add__(self, other):  # +
        return self.x + other.x

    def __iadd__(self, other):  # +=
        tmp = self.x + other.x
        return tmp
    def __mul__(self, other):   # *
        return self.x * other.x

    def __imul__(self, other):   # *=
        tmp = self.x * other.x
        return tmp

    def __truediv__(self, other):  # /
        return self.x / other.x

    def __itruediv__(self, other):   # /=
        tmp = self.x / other.x
        return tmp

    def __mod__(self, other):       # %
        return self.x % other.x

    def __imod__(self, other):      # %=
        tmp = self.x % other.x
        return tmp

    def __floordiv__(self, other):  # //
        return self.x // other.x

    def __ifloordiv__(self, other):  # //=
        tmp = self.x // other.x
        return tmp

    def __pow__(self, power, modulo=None):   # **
        return self.x ** power

    def __ipow__(self, other):        # **=
        tmp = self.x ** other.x
        return tmp

    def __str__(self):
        return str(self)


x = A(5)
y = A(3)
print(x - y, x.__sub__(y))
print(x + y, x.__add__(y))
print(x - y, x.__isub__(y))
print(x - y, x.__iadd__(y))
print(x * y, x.__mul__(y))
print(x / y, x.__truediv__(y))
print(x // y, x.__ifloordiv__(y))

