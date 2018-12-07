#-*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import scipy as sp
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from numpy import nan as NA
from scipy.stats import ks_2samp

# data = pd.read_csv('C:\\Users\\Public\\xb.csv')
# data = data.dropna(axis=0, how='any')


# data = pd.read_csv('C:/Users/luna/Desktop/bsd/shandietest.csv')
data = pd.read_excel('C:/Users/luna/Desktop/bsd/好坏测试名单.xlsx')
data = data.drop(['姓名', '身份证', '手机号'], axis=1)


data = data.dropna(axis=0, how='any')

#构建X变量和Y变量
x_feature = list(data.columns)
x_feature.remove('Creditability')
x = data[x_feature]
y = data['Creditability']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
clf = tree.DecisionTreeRegressor()
print(clf)
clf.fit(x_train,y_train)

prob = clf.predict(x_test)
df = pd.DataFrame()
df['Creditability'] = y_test
df['Creditability'] = prob
print(df.head())

print('**************************importance*****************************')
importances =clf.feature_importances_
importance = pd.DataFrame()
for i in range(len(x_feature)):
    importance['feature'] = x_feature
    importance['importance'] = importances
# importance.to_csv('C:/Users/Administrator/Desktop/yd_tags_importance_result.csv'
importance_n = importance.loc[importance['importance'] > 0.02]
print(importance_n)


print('****************************ks_value*******************************')
get_ks = lambda y_pred, y_true: ks_2samp(y_pred[y_true == 1], y_pred[y_true != 1]).statistic
ks = get_ks(prob,y_test)
print(ks)
