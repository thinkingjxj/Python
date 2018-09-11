import math


class Shape:
    @property
    def area(self):
        return


class Triangle(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def area(self):
        return self.x * self.y * 1/2


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    @property
    def area(self):
        return self.r**2*math.pi


class Rectang:
    def __init__(self):
        pass

    @property
    def area(self):
        pass
