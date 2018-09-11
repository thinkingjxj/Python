# 下面是上课讲的
# 记录车的品牌mark、颜色color、价格price、速度speed等特征，
# 并实现增加车辆信息、显示全部车辆信息的功能  # 数据在哪操作在哪

class Car:
    def __init__(self, mark, color, price, speed):
        self.__mark = mark
        self.__color = color
        self.__price = price
        self.__speed = speed


class CarInfo:
    def __init__(self):
        self.lst = []

    def addcar(self, car: Car):  # 认知不足之处car是类Car
        self.lst.append(car)

    def getall(self):
        return self.lst


c1 = CarInfo()
car = Car('audi', 400, 'black', 100)
c1.addcar(car)
c1.getall()  # 返回所有数据，此时实现格式打印
print(c1.getall())


# class CarInfo:
#     lst = []   # 放这里不太好，类的属性，放到实例里面会更好
#     def __init__(self):
#         pass
#     def addcar(self, car:Car):
#         self.lst.append(car)
#     def getall(self):
#         return self.lst   # 打印格式
# c1 = CarInfo()
# car = Car('audi', 400, 'black', 100)
# c1.addcar(car)
# c1.getall()
