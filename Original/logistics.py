import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from scipy.stats import ks_2samp
import numpy as np
from sklearn.externals import joblib

# data = pd.read_csv('C:\\Users\\Public\\xb.csv')
# data = data.dropna(axis=0, how='any')

# data = pd.read_csv('C:/Users/luna/Desktop/bsd/shandietest.csv')
# data = data.dropna(axis=0, how='any')

data = pd.read_excel('C:/Users/luna/Desktop/bsd/好坏测试名单.xlsx')
data = data.drop(['身份证'], axis=1)
data = data.dropna(axis=0, how='any')
data = data.fillna(0)

# 构建X变量和Y变量
x_feature = [i for i in data.columns if i not in ['good']]
x = data[x_feature]
y = data['good']
print(len(y))


# 测试用，对数据进行0-1标准化
def zero_one_scaler(data):
    data_2 = (data - data.min()) / (data.max() - data.min())
    return data_2


# x = (x-x.min())/(x.max()-x.min())
# X = zero_one_scaler(x)
# print(x.head())

def train_validation_split(x, y, test_size=0.3):
    y_m = pd.DataFrame(y)
    y_m.columns = ['true_value']
    data = x.join(y_m)

    x_train = pd.DataFrame()
    x_test = pd.DataFrame()
    y_train = pd.Series()
    y_test = pd.Series()

    y_set = set(y)
    for i in y_set:
        dataset = data[data['true_value'] == i]
        y = dataset['true_value']
        x_feature = list(dataset.columns)
        x_feature.remove('true_value')
        x = dataset[x_feature]
        x_train_m, x_test_m, y_train_m, y_test_m = train_test_split(x, y, test_size=test_size)
        x_train = pd.concat([x_train, x_train_m])
        x_test = pd.concat([x_test, x_test_m])
        y_train = pd.concat([y_train, y_train_m])
        y_test = pd.concat([y_test, y_test_m])
    return x_train, x_test, y_train, y_test


lr = LogisticRegression(max_iter=50, C=1.0, tol=0.01)  # 这里使用了默认的参数设置
print('*******************参数设置**********************')
print(lr)

if __name__ == '__main__':
    X = zero_one_scaler(x)
    x_train, x_test, y_train, y_test = train_validation_split(X, y, test_size=0.3)
    lr.fit(x_train, y_train)
    y_predict = lr.predict_proba(x_test)[:, 1]
    x_predict = lr.predict_proba(x_train)[:, 1]
    df = pd.DataFrame()
    df['status'] = y_test
    df['prob'] = y_predict

    # df.to_csv('C:\\Users\\qiaoli zhang\\Desktop\\R语言\\mm.csv')
    joblib.dump(lr, 'C:\\Users\\Public\\lr.pkl')
    print('****************************ks_value*******************************')
    get_ks = lambda y_pred, y_true: ks_2samp(y_pred[y_true == 1], y_pred[y_true != 1]).statistic
    ks = get_ks(y_predict, y_test)
    ks1 = get_ks(x_predict, y_train)
    print(ks)
    print(ks1)
    print('k-s差值:', ks1 - ks)

    result = pd.DataFrame()
    result['log_train_value'] = list(x_predict)
    result['real_train_value'] = list(y_train)
    result1 = pd.DataFrame()
    result1['log_test_value'] = list(y_predict)
    result1['real_test_value'] = list(y_test)

    result.to_csv('C:\\Users\\Public\\train_xinbing_KS.csv')
    result1.to_csv('C:\\Users\\Public\\test_xinbing_KS.csv')
