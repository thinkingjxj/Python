import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from scipy import stats


d = pd.read_excel('C:/Users/luna/Desktop/d.xlsx')
print(d)


rng = np.random.RandomState(42)
n_samples = 6   #样本总数

clf = IsolationForest(max_samples=n_samples, random_state=rng, contamination=0.33)
clf.fit(d.values)
scores_pred = clf.decision_function(d.values)
# decision_function返回样本的异常评分，值越小表示越有可能是异常样本
print(scores_pred)
print(len(scores_pred))

# threshold = stats.scoreatpercentile(scores_pred, 100* outliers_fraction)
print(clf.predict(d.values))




