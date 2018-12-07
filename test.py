import pandas as pd

d = pd.read_csv('C:/Users/luna/Desktop/bsd/shandietest.csv')

# d = d[~d['雨点分'].isin([-1])]  # 删除-1的行

print(d.head(3))
# print(d)
# print(d.shape)
