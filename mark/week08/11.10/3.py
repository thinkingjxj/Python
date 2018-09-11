# shape基类，要求所有子类都必须提供面积的计算，子类有三角形、矩形、圆
# 圆类的数据可序列化
import math


class Shape:
    def area(self):
        pass


class Triangle(Shape):
    def __init__(self, a, h):
        self.a = a
        self.h = h

    def area(self):
        self.__area = 1 / 2 * self.a * self.h
        return self.__area


class Rectang(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        self.__area = self.a * self.b
        return self.__area


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        self.__area = math.pi * (self.r ** 2)
        return self.__area
