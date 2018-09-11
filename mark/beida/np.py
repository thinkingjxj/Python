import numpy as np


# 数列的范围和步长
n = np.arange(0,2,0.5)
print(n)

# 范围与个数
a = np.linspace(-1,0,6)
print(a)

# b = np.arange(6)           # 1d array
# print(b)
#
# c = np.arange(12).reshape(4,3)   # 2d array
# print(c)
#
# d = np.arange(24).reshape(2,3,4)   # 3d array
# print(d)

b = np.arange(12).reshape(3,4)
print(b)
print(b.sum(axis=1))


