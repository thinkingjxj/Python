import pandas as pd
from sklearn.decomposition import PCA
# from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import matplotlib.pyplot as plt


# lda = LinearDiscriminantAnalysis(n_components=15)


d = pd.read_excel('C:/Users/luna/Desktop/test.xlsx')

# print(d.head(3))

d = d.drop(['身份证', 'good'], axis=1)
d = d.dropna(axis=0, how='any')
d = d.fillna(0)

plt.figure()

print(d.shape)
pca = PCA(whiten=True)
m = pca.fit(d)
print(m)
print(type(m))
print(pca.explained_variance_)   # 代表降维后的各主成分的方差值，越大，说明越是重要的主成分
print(len(pca.explained_variance_))
print(pca.explained_variance_ratio_)   # 代表降维后的各主成分的方差值占总方差值的比例，这个比例越大，则越是重要的成分、
print(len(pca.explained_variance_ratio_))

plt.plot(range(50), pca.explained_variance_)
plt.plot(range(50), pca.explained_variance_ratio_)
plt.show()
# print(d.head(3))
# print(d.columns)
# d.corr().to_csv('C:/Users/luna/Desktop/bsd/g_b_corr.csv', encoding='ANSI')





















