import random

class Rd:
    def __init__(self, min=1, max=100, count=15):
        self.min = min
        self.max = max
        self.count = count
        self.g = self._generate()   # 生成器对象

    def _generate(self):
        while True:
            yield [random.randint(self.min, self.max) for _ in range(self.count)]
    def generate(self, count):
        self.count = count
        return next(self.g)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

d = Rd()
lst = d.generate(10)
print(lst)

m = [Point(k,v) for k, v in zip(d.generate(10), d.generate(10))]

for p in m:
    print(p.x, p.y)

