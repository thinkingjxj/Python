# filter(function, iterable)
# 过滤可迭代对象的元素， 返回一个迭代器
# function一个具有一个参数的函数，返回bool
c = list(filter((lambda x: x % 3 == 0), [1, 9, 55, 150, -3, 28, 124]))
print(c)


# map(function, *iterable) --> map object
# 将多个可迭代对象的元素按照指定的函数进行映射，返回一个迭代器

a = list(map((lambda x: 2*x + 1), range(5)))
print(a)
b = dict(map((lambda x: (x%5,x)), range(500)))
print(b)
