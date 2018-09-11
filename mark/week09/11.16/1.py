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
        return 'Point: {}, {}'.format(self.x, self.y)


a = Point(1, 6)
b = Point(2, 7)
points = (a, b)
print(points[0].add(points[1]))   # Point:3,13
# 运算符重载
print(points[0] + points[1])      # (3,13)  __add__
print(Point(*(points[0] + points[1])))      #Point: 3, 13    __add__
print(a == b)                           # False

# 运算符重载应用场景
# 往往是用面向对象实现的类，需要做大量的运算，而运算符是这种运算在数学上最常见的方式。
# 例如，上例中的对+进行了运算符重载，实现了Point类的二元操作，重新定义为Point+Point
# 提供运算符重载，比直接提供加法方法要更加适合该领域内使用者的习惯
# ini类，几乎实现了所有操作符，可以作为参考

