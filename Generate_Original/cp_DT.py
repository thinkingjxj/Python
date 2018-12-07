
import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
from scipy.stats import ks_2samp


data = pd.read_csv('C:/Users/luna/Desktop/bsd/shandietest.csv')
data = data.dropna(axis=0, how='any')

#构建X变量和Y变量
x = data.drop(['Creditability'], axis=1)
y = data['Creditability']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
clf = tree.DecisionTreeRegressor()
clf.fit(x_train, y_train)

prob = clf.predict(x_test)
# prob = pd.DataFrame(prob, columns=['Creditability'])

print('**************************importance*****************************')
importance = clf.feature_importances_
importance = pd.DataFrame(importance, columns=['importance'])
importances = pd.concat([importance, pd.DataFrame((data.columns), columns=['features'])], axis=1)
importance_n = importances.loc[importances['importance'] > 0.02]
print(importance_n)

print('****************************ks_value*******************************')
get_ks = lambda y_pred, y_true: ks_2samp(y_pred[y_true == 1], y_pred[y_true != 1]).statistic
ks = get_ks(prob,y_test)
print(ks)

