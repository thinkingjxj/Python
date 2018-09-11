from collections import Hashable


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


p1 = Point(4, 5)
p2 = Point(4, 5)
print(hash(p1))
print(hash(p2))  # p1,p2哈希值一样
print(p1 is p2)  # False
print(p1 == p2)  # True
print(set((p1, p2)))

print(isinstance(p1, Hashable))  # True
