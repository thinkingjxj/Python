import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

diabetes = datasets.load_diabetes()

# use only the feature
diabetes_X = diabetes.data[:, np.newaxis, 2]

# split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# split the targets into training/testing sets
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

# create linear regression object
regr = linear_model.LinearRegression()

# train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)

# make predictions using the testing set
diabetes_y_pre = regr.predict(diabetes_X_test)

# the coefficients
print('Coefficients: \n', regr.coef_)
# the mean squared error
print('Mean squared error: %.2f' % mean_squared_error(diabetes_y_test, diabetes_y_pre))
# explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(diabetes_y_test, diabetes_y_pre))

# plot outputs
plt.scatter(diabetes_X_test, diabetes_y_test, color='black')
plt.plot(diabetes_X_test, diabetes_y_pre, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
