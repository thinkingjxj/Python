import numpy as np
import pandas as pd

fp = 'data.xlsx'    # 当前目录下没有数据
data = pd.read_excel(fp, index_col=None, header=None, encoding='utf8')
m, n = data.shape
print(m, n)
data = data.as_matrix(columns=None)    # 将DataFrame格式转换为matrix格式
print(data)

k = 1/ np.log(m)
yij = data.sum(axis=0)

pij = data / yij   # 计算pij

test = pij * np.log(pij)
test = np.nan_to_num(test)
ej = -k * (test.sum(axis=0))    # 计算各个指标的信息熵

wi = (1 - ej) / np.sum(1-ej)
print(wi)
