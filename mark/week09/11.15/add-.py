class A:
    def __init__(self, a):
        self.a = a

    def __sub__(self, other):
        return self.a - other.a

    def __isub__(self, other):
        tmp = self.a - other.a
        return A(tmp)

    def __str__(self):
        return str(self.a)


X = A(5)
Y = A(4)
print(X - Y, X.__sub__(Y))

X -= Y  # X = X - Y
print(X)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __add__(self, other):
        return (self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return 'Point: {},{}'.format(self.x, self.y)
