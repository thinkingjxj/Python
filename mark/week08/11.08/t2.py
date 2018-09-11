import random

# class Rd:
#     @classmethod
#     def count(cls, min=1, max=100, count=10):
#         return [random.randint(min, max) for _ in range(count)]
# 随机整数生成类，可以指定一批生成的个数，可以指定数值的范围，可以调整每批生成数字的个数
# 使用上题中的类，随机生成20个数字，两两配对形成二维坐标系的坐标，把这些坐标组织起来，并打印输出


class Rd:

    def __init__(self, min=1, max=100, count=10):
        self.min = min
        self.max = max
        self.count = count
        self.rg = self._generate()

    def _generate(self):
        while True:
            yield [random.randint(self.min, self.max) for _ in range(self.count)]

    def generate(self, count):
        self.count = count        # 覆盖前面的
        return next(self.rg)

r = Rd()
lst = r.generate(10)
print(lst)


#
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __str__(self):
        return '{}:{}'.format(self.x, self.y)
    #
    # def __reduce__(self):
    #     return '{}:{}'.format(self.x, self.y)


lst1 = [Point(*v) for v in zip(r.generate(10), r.generate(10))]
#lst1 = [Point(k, v) for k, v in zip(r.generate(10), r.generate(10))]
print(lst1)  # 打出来不是我们期望看到的


for p in lst1:
    print(p.x, p.y)

