class Fib:
    def __init__(self):
        self.lst = [0, 1, 1]

    def __len__(self):
        return len(self.lst)

    def __call__(self, x):
        if x < len(self.lst):
            return self.lst
        for i in range(len(self.lst)-1, x):  # 2修改为len(self.lst)-1，不然后面实例化调用会出问题
            self.lst.append(self.lst[i-1] + self.lst[i])
        return self.lst

    def __getitem__(self, item):    # item是index
        if item < 0:
            return None
        if item < len(self):
            return self.lst[item]
        self(item)                  # 调用

    def __iter__(self):
        return iter(self.lst)


a = Fib()
print(a(5))
print(a(7))
print(a(4))
print(a(3))
#print(a([3]))
print(a.__getitem__(3))

