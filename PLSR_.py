from sklearn.cross_decomposition import PLSRegression



x = [[0., 0., 1.],
     [1., 0., 0.],
     [2., 2., 2.],
     [2., 5., 4.]]
y = [[0.1, -0.2],
     [0.9, 1.1],
     [6.2, 5.9],
     [11.9, 12.3]]


pls = PLSRegression(n_components=2)
b = pls.fit(x, y)
print(b)

y_pred = pls.predict(x)
print(y_pred)
print(y)


y_t = pls.fit_transform(y)   # learn and apply the dimension reduction on the train data
print(y_t)
# pls.get_params(deep=True)    # get parameters for this estimator
# pls.score(x, y)    # returns the coefficient of determination r^2 of the prediction
# pls.set_params()    # set the parameters of this estimator
# pls.transform(x)    # apply the dimension reduction learned on the train data
#


