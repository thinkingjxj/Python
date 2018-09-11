class Point:
    Z = 5
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __delattr__(self, item):
        print('Can not del {}'.format(item))

p = Point(1, 8)
del p.x
p.z = 15
del p.z
del p.Z
print(p.__dict__)
# print(Point.__dict__)

