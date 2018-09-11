class Item:
    def __init__(self, name, **kwargs):
        self.name = name
        self._spec = kwargs

    def __repr__(self):
        return str(self)


class Cart:
    def __init__(self):
        self.lst = []

    def additem(self, item):
        self.lst.append(item)

    def __add__(self, other):  # 不同类型之间的
        print(other)
        self.lst.append(other)
        return self

    def __getitem__(self, index):  # 如果为字典index修改为字典的key
        # print(index)              # item此时为索引
        return self.lst[index]

    def __setitem__(self, key, value):
        # print(key, value)
        self.lst[key] = value
        # self[key] = value  # 出错，调用getitem：value = value

    def __iter__(self):  # 返回必须是迭代器
        return iter(self.lst)

    def __len__(self):
        return len(self.lst)

    def __str__(self):
        return str(self.lst)

    # def __missing__(self, key):   # 字典才有此方法
    #     print(key)


c = Cart()
c.__add__('coat')
c.__add__('shoes')
print(c.lst)


# 链式编程


# 练习字典
class MyDict(dict):
    pass