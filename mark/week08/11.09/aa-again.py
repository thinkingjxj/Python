class Car:
    def __init__(self, mark, color, price, speed):
        self.mark = mark
        self.price = price
        self.color = color
        self.speed = speed


class CarInfo:
    def __init__(self):
        self.lst = []

    def addcar(self, car: Car):
        return self.lst.append(car)

    def getcar(self):
        return self.lst


c = CarInfo()
d = Car('audi', 'black', '100', 400)
c.addcar(d)
for p in c.getcar():
    print(p)
