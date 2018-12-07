import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from scipy.stats import ks_2samp
from sklearn.externals import  joblib


data = pd.read_csv('C:/Users/luna/Desktop/bsd/shandietest.csv')
data = data.dropna(axis=0, how='any')

# 构建X变量和Y变量
x = data.drop(['Creditability'], axis=1)
y = data['Creditability']


# 测试用，对数据进行0-1标准化
def zero_one_scaler(data):
    data_2 = (data - data.min()) / (data.max() - data.min())
    return data_2

X = zero_one_scaler(x)

y_m = pd.DataFrame(y, columns=['true_value'])
d = x.join(y_m)

y_set = set(y)
print(y_set)
x_train = pd.DataFrame()

for i in y_set:
    dataset = d[d['true_value'] == i]
    y = dataset['true_value']
    # x_feature = list(dataset.columns)
    # x_feature.remove('true_value')
    x = dataset.drop(['true_value'], axis=1)
    x_train_m, x_test_m, y_train_m, y_test_m = train_test_split(x, y, test_size=0.3)
    x_train = pd.concat([x_train, x_train_m])
# print(x_train)
    # x_test = pd.concat([x_test, x_test_m])
    # y_train = pd.concat([y_train, y_train_m])
    # y_test = pd.concat([y_test, y_test_m])




# def train_validation_split(x, y, test_size=0.3):
#     y_m =
#     # y_m.columns = ['true_value']
#     data = x.join(y_m)
#
#     x_train = pd.DataFrame()
#     x_test = pd.DataFrame()
#     y_train = pd.Series()
#     y_test = pd.Series()
#
#     y_set = set(y)    # 真实值
#     print(y_set)
#     for i in y_set:
#         dataset = data[data['true_value']==i]
#         y = dataset['true_value']
#         x_feature = list(dataset.columns)
#         x_feature.remove('true_value')
#         x = dataset[x_feature]
#         x_train_m, x_test_m, y_train_m, y_test_m = train_test_split(x, y, test_size=test_size)
#         x_train = pd.concat([x_train, x_train_m])
#         x_test = pd.concat([x_test, x_test_m])
#         y_train = pd.concat([y_train, y_train_m])
#         y_test = pd.concat([y_test, y_test_m])
#     return x_train, x_test, y_train, y_test


# x_train, x_test, y_train, y_test = train_validation_split(X, y, test_size=0.3)

