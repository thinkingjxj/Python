# import pandas as pd
# d = pd.read_excel('C:/Users/luna/Desktop/bsd/test_report/贷后雷达测试报告.xlsx')
# # print(d.head())
# print(d.corr())
# d.corr().to_csv('C:/Users/luna/Desktop/bsd/test_report/corr_loans.csv', encoding='ANSI')

from sklearn.model_selection import cross_val_score
from sklearn.datasets import make_blobs
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

X,y = make_blobs(n_samples=10000, n_features=10, centers=100, random_state=0)
print(len(X))
print(len(y))

clf = DecisionTreeClassifier(max_depth=None, min_samples_split=2, random_state=0)
scores = cross_val_score(clf, X, y)
print(scores.mean())

# plt.figure()
# plt.plot(X, y)
# plt.show()

cf = RandomForestClassifier(n_estimators=10, max_depth=None, min_samples_split=2, random_state=0)
score = cross_val_score(cf, X, y)
print(score.mean())


c = ExtraTreesClassifier(n_estimators=10, max_depth=None, min_samples_split=2, random_state=0)
score = cross_val_score(c, X, y)
print(score.mean())









