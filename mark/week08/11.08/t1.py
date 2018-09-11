import random

class Rd:
    def __init__(self, min=1, max=100, count=15):
        self.min = min
        self.max = max
        self.count = count
        self.rg = self._generate()    # 认知不足之处：类方法在前，实例在后

    def _generate(self):
        while True:
            yield [random.randint(self.min, self.max) for _ in range(self.count)]

    def generate(self, count):
        self.count = count
        return next(self.rg)

r = Rd()
lst = r.generate(10)
print(lst)

# 列表中20个数两两形成坐标,利用zip函数
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 局限性之处：想不到用zip函数，且坐标与上面的类联系在一起
lst1 = [Point(k, v) for k, v in zip(r.generate(10), r.generate(10))]
print(lst1)  # 打印出来是对象

for p in lst1:
    print(p.x, p.y)
