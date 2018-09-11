class Cart:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def additem(self, item):
        self.items.append(item)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, item):
        return self.items[item]

    def __setitem__(self, key, value):
        self.items[key] = value


cart = Cart()
cart.additem(1)
cart.additem('a')
for i in range(2, 5):
    cart.additem(i)
cart.additem('b')

print(len(cart))
for x in cart:
    print(x)
print(2 in cart)

print(cart[1])
cart[3] = 'c'
print(cart[3])
