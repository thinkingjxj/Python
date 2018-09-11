# 自己写的，没达到要求，查看摄氏温度和华氏温度之间的关系
class Temperature:
    def __init__(self, c=15):
        self.c = c

    def trans(self, f):
        self.c = 5 * (f-32) / 9
        return self.c

class Tp:
    def __init__(self, f=40):
        self.f = f

    def trans(self, c):
        self.f = 9 * c / 5 + 32
        return self.f


s1 = Temperature()
print(s1.trans(40))

s2 = Tp()
print(s2.trans(4.4))

