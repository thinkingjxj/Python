import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.calibration import CalibratedClassifierCV
from sklearn.metrics import log_loss
import random

random.seed(0)
X, y = make_blobs(n_samples=1000, n_features=2, random_state=42, cluster_std=5.0)

X_train, y_train = X[:600], y[:600]
X_valid, y_valid = X[600:800], y[600:800]
X_train_valid, y_train_valid = X[:800], y[:800]
X_test, y_test = X[800:], y[800:]
# print(y_test)

# train uncalibrated random forest classifier on whole train and validation data and evaluate on test data
clf = RandomForestClassifier(n_estimators=25)
clf.fit(X_train_valid, y_train_valid)
clf_probs = clf.predict_proba(X_test)
print('clf_prob.shape: ', clf_probs.shape)  # 200, 3
score = log_loss(y_test, clf_probs)
print('score: ', score)

clf = RandomForestClassifier(n_estimators=25)
clf.fit(X_train, y_train)
clf_probs = clf.predict_proba(X_test)
sig_clf = CalibratedClassifierCV(clf, method='sigmoid', cv='prefit')
sig_clf.fit(X_valid, y_valid)
sig_clf_probs = sig_clf.predict_proba(X_test)
sig_score = log_loss(y_test, sig_clf_probs)
print('sig_score: ', sig_score)

plt.figure()
colors = ['r', 'g', 'b']
for i in range(clf_probs.shape[0]):
    plt.arrow(clf_probs[i, 0], clf_probs[i, 1],
              sig_clf_probs[i, 0] - clf_probs[i, 0],
              sig_clf_probs[i, 0] - clf_probs[i, 1],
              color= colors[y_test[i]], head_width=1e-2)

# plot perfect predictions
plt.plot([1.0], [0.0], 'ro', ms=20, label='Class 1')
plt.plot([0.0], [1.0], 'go', ms=20, label='Class 2')
plt.plot([0.0], [0.0], 'bo', ms=20, label='Class 3')

# plot boundaries of unit simplex
plt.plot([0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], 'k', label='Simplex')

# Annotate points on the simplex
plt.annotate(r'($\frac{1}{3}$, $\frac{1}{3}$, $\frac{1}{3}$)',
             xy=(1.0/3, 1.0/3), xytext=(1.0/3, .23), xycoords='data',
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='center', verticalalignment='center')
plt.plot([1.0/3], [1.0/3], 'ko', ms=5)



plt.show()


























