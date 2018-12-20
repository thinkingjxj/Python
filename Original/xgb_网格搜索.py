import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor
from scipy.stats import ks_2samp
from sklearn import preprocessing
from sklearn import metrics
from xgboost.sklearn import XGBRegressor
from sklearn import utils
from numpy import nan as NA
from sklearn.externals import joblib




# 按比例划分好坏样本的训练集和测试集
# def train_validation_split(x, y, test_size=0.2):
#     y_m = pd.DataFrame(y)
#     y_m.columns = ['real_value']
#     # y_m = pd.DataFrame(y, columns=['real_value'])
#     data = x.join(y_m)
#     x_train = pd.DataFrame()
#     x_test = pd.DataFrame()
#     y_train = pd.Series()
#     y_test = pd.Series()
#     y_set = set(y)  # y值的集合
#     for i in y_set:
#         dataset = data[data['real_value'] == i]
#         y = dataset['real_value']
#         x_feature = list(dataset.columns)
#         x_feature.remove('real_value')
#         x = dataset[x_feature]
#         x_train_m, x_test_m, y_train_m, y_test_m = train_test_split(x, y, test_size=test_size)
#         x_train = pd.concat([x_train, x_train_m])
#         x_test = pd.concat([x_test, x_test_m])
#         y_train = pd.concat([y_train, y_train_m])
#         y_test = pd.concat([y_test, y_test_m])
#     return x_train, x_test, y_train, y_test


# 从训练集中随机选择部分（good_size）好样本与坏样本进行cycle_num次预测，计算平均值

def good_bad_split(x, y, good_label=0, bad_label=1, good_size=0.6, bad_size=0.6):
    y_m = pd.DataFrame(y)
    y_m.columns = ['real_value']
    # y_m = pd.DataFrame(y, columns=['real_value'])
    data = x.join(y_m)
    # x_train = pd.DataFrame()
    # x_test = pd.DataFrame()
    # y_train = pd.Series()
    # y_test = pd.Series()
    x_feature = list(data.columns)
    x_feature.remove('real_value')

    good_set = data[data['real_value'] == good_label]
    y_good = good_set['real_value']
    x_good = good_set[x_feature]
    x_good_train, x_good_test, y_good_train, y_good_test = train_test_split(x_good, y_good, test_size=good_size)

    bad_set = data[data['real_value'] == bad_label]
    y_bad = bad_set['real_value']
    x_bad = bad_set[x_feature]
    x_bad_train, x_bad_test, y_bad_train, y_bad_test = train_test_split(x_bad, y_bad, test_size=bad_size)

    x_train = pd.concat([x_good_test, x_bad_test])
    x_test = pd.concat([x_good_train, x_bad_train])
    y_train = pd.concat([y_good_test, y_bad_test])
    y_test = pd.concat([y_good_train, y_bad_train])
    good_len = len(x_good_test)
    bad_len = len(x_bad_test)
    return x_train, x_test, y_train, y_test, good_len, bad_len


if __name__ == '__main__':
    data = pd.read_csv('C:\\Users\\Public\\ceshi\\xinyanbingjianzonghe.csv',encoding = 'ANSI')
    # data = data.fillna(9999)
    # data['day'] = data.days.apply(lambda x: 1 if x > 3 else 0)
    x_feature = [i for i in data.columns if i not in['Creditability']] # 移除无关数据
    # data['pro_level'] = data['pro_level'].map({'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10})
    data = data.dropna(axis=0, how='any')
    print(data.columns)
    print(x_feature)
    x = data[x_feature]
    # x = data.drop(['D4'], 1)
    # print(x.head())
    y = data['Creditability']

    # 对数据进行标准化，选择标准化方式
    # X = min_max_scaler(x)
    x_train, x_test, y_train, y_test, good_len, bad_len = good_bad_split(x, y)
    print(good_len, bad_len)

    reg = XGBRegressor(learning_rate=0.1, n_estimators=30, max_depth=4, min_child_weight=4, gamma=0.1,
                       subsample=0.9, colsample_bytree=0.8, objective='binary:logistic', reg_alpha=1,
                       scale_pos_weight=1, seed=27)
    param_test = [{
        'max_depth': [i for i in range(1, 3)],
        # 'min_child_weight': range(1, 5),
        'gamma': [i / 10.0 for i in range(0, 10)],
        # 'subsample': [i / 10.0 for i in range(8, 10)],
        # 'colsample_bytree': [i / 10.0 for i in range(8, 10)],
        # 'reg_alpha': [1e-5, 1e-2, 0.1, 1, 100],
        'n_estimators': [i for i in range(2, 14, 2)],
        # 'learning_rate': np.linspace(0.9, 1.1, 5),
    }]
    gsearch = GridSearchCV(reg, param_grid=param_test, scoring='neg_mean_squared_error', n_jobs=4, iid=False, cv=5)

    gsearch.fit(x_train, y_train)  # 进行模型的训练
    # for i in gsearch.grid_scores_:
    #     print(i)
    print('********************best_params********************')
    print(gsearch.best_params_)
    print('********************best_score********************')
    print(gsearch.best_score_)
    print('********************best_estimator********************')
    print(gsearch.best_estimator_)
    best_model = gsearch.best_estimator_
    joblib.dump(best_model, 'sxh_xy_1.pkl')
    test_predict = best_model.predict(x_test)
    importance = best_model.feature_importances_
    for i in range(len(importance)):
        print(x_feature[i], importance[i])
    # print(importance)
    get_ks = lambda y_predict, y_test: ks_2samp(y_predict[y_test == 1], y_predict[y_test != 1]).statistic
    train_predict = best_model.predict(x_train)
    ks_train = get_ks(train_predict, y_train)
    ks_test = get_ks(test_predict, y_test)
    print('XGB train k-s值:', ks_train)
    print('XGB test k-s值:', ks_test)
    print('k-s差值:', ks_train-ks_test)
    result = pd.DataFrame()
    result['XGB_train_value'] = list(train_predict)
    result['real_train_value'] = list(y_train)
    result1 = pd.DataFrame()
    result1['XGB_test_value'] = list(test_predict)
    result1['real_test_value'] = list(y_test)

    result.to_csv('C:\\Users\\Public\\train_data_KS.csv')
    result1.to_csv('C:\\Users\\Public\\test_data_KS.csv')

