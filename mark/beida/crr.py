import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel(r'C:\Users\余雪鹏\Desktop\yu\1.xlsx')
print(data.head())

# 空值填充
# data=data.fillna(0)
print(data.isnull().sum())

# 输出指定列的相关系数
print("U1列和U2列的相关系数", data.U1.corr(data.U2))
print("U1列和U2列的相关系数", data.U1.cov(data.U2))

# 返回一个相关系数矩阵
# print("整体的协方差矩阵",data.corr())

# 读取指定行
print(data.loc[0])
# print(data.loc[1])

# 删除time列
data = data.drop('time', axis=1)
# print("删除指定列",data)
data = data.drop([56, 57, 58])
data = data.drop([12, 19])
print(data.head(56))

# 索引重排
data = data.reset_index(drop=True)
print(data.head(54))

for i in range(0, 54, 1):
    print("第0行与第%d行的相关系数：%f" % (i, data.loc[0].corr(data.loc[i])))

# 行之间相关系数的排序，
covlist = []
for i in range(0, 54, 1):
    covlist.append(data.loc[0].corr(data.loc[i]))
# print(covlist)
print(sorted(covlist, reverse=True))

# 画图分析一下行之间的关系
'''
fig=plt.figure()
ax=fig.add_subplot(111)
ax.scatter(data.loc[0],data.loc[4])
#plt.show()


fig=plt.figure()
plt.plot(data.loc[0],data.loc[1])
plt.show()
'''
data = data.fillna(0)
# print(data.isnull().sum())

# 以第一行数据为基准，
fig = plt.figure()
sns.distplot(data.loc[0])
plt.xlabel("first data")
plt.show()

# 对比
plt.subplot(221)
plt.scatter(range(data.shape[1]), data.loc[20])
plt.xlabel("1 and 20")
plt.subplot(222)
plt.scatter(range(data.shape[1]), data.loc[4])
plt.xlabel("1 and 4")
plt.subplot(223)
plt.scatter(range(data.shape[1]), data.loc[52])
plt.xlabel("1 and 52")
plt.subplot(224)
plt.scatter(range(data.shape[1]), data.loc[52])
plt.xlabel("1 and 53")
plt.show()

# 对列重命名，方便对比相关系数
# data=data.rename(lambda x: x[1:],axis='columns')
# print(data.head())


# 列和列之间的相关性分析
data_corr = data.corr().abs()
print(data_corr.U1.sort_values(ascending=False)[:10])

plt.subplot(231)
plt.scatter(range(data.shape[0]), data.U2.values)
plt.xlabel("U1 and U2")
plt.subplot(232)
plt.scatter(range(data.shape[0]), data.U3.values)
plt.xlabel("U1 and U2")
plt.show()
