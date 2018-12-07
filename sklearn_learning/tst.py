import seaborn as sns   # visualization tool
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score


d = pd.read_csv('C:/Users/luna/Desktop/creditcard.csv')
print(d.shape)
# print(d.head(5))

plt.figure(figsize=(16, 7))
sns.lmplot(x='Amount', y='Time', hue='Class', data=d)

plt.figure(figsize=(16,7))
plt.scatter(x='Time', y='Amount', data=d[d['Class'] == 1])
plt.xlabel('Time')
plt.ylabel('Amount')
plt.show()


X = d.drop('Class', axis=1)
y = d['Class']

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
lr = LogisticRegression()
lr.fit(x_train, y_train)
y_pred = lr.predict(x_test)

print('Train score: {}'.format(lr.score(x_train, y_train)))
print('Test score: {}'.format(lr.score(x_test, y_test)))

scores = cross_val_score(lr, X, y)
print('Cross-validation scores: {}'.format(scores))


print('Confusion Matrix: ')
print(confusion_matrix(y_test, y_pred))

print('Accuracy Score: ')
print(accuracy_score(y_test, y_pred))






