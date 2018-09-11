# 模拟购物车购物
class Color:
    red = 0
    blue = 1
    green = 2
    golden = 3
    black = 4
    other = 1000


class Item:
    def __init__(self, **kwargs):  # 局限性，想不到用**kwargs
        self._spc = kwargs

    def __repr__(self):
        return str(sorted(self._spc.items()))


class Cart:
    def __init__(self):
        self.items = []

    def additem(self, item: Item):
        self.items.append(item)

    def getallitems(self):
        return self.items


mycart = Cart()
myphone = Item(mark='Huawei', color=Color.golden, memory='4G')
mycart.additem(myphone)

mycar = Item(mark='Red Flag', color=Color.black, year=2017)
mycart.additem(mycar)

print(mycart.getallitems())
