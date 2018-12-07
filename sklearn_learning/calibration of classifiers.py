import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.calibration import calibration_curve


X, y = datasets.make_classification(n_samples=100000, n_features=20, n_informative=2, n_redundant=2)
print(X.shape)
print(y.shape)
train_samples = 100

x_train = X[:train_samples]
x_test = X[train_samples:]
y_train = y[:train_samples]
y_test = y[train_samples:]

# create classifiers
lr = LogisticRegression()
gnb = GaussianNB()
svc = LinearSVC()
rfc = RandomForestClassifier(n_estimators=100)


# plot calibration plots
plt.figure()
ax1 = plt.subplot2grid((3, 1), (0, 0), rowspan=2)
ax2 = plt.subplot2grid((3, 1), (2, 0))

ax2.plot([0, 1], [0, 1], 'k:', label='Perfect calibrated')
for clf, name in [(lr, 'Logistic'),
                  # (gnb, 'Naive Bayes'),
                  (svc, 'Support Vector Classification'),
                  # (rfc, 'Random Forest')
                  ]:
    clf.fit(x_train, y_train)
    if hasattr(clf, 'predict_prob'):
        probs_pos = clf.predict_prob(x_test)[:, 1]
    else:   # use decision function
        probs_pos = clf.decision_function(x_test)
        probs_pos = (probs_pos - probs_pos.min()) / (probs_pos.max() - probs_pos.min())

    fraction_of_positives_value, mean_predicted_value = calibration_curve(y_test, probs_pos, n_bins=10)
    ax1.plot(mean_predicted_value, fraction_of_positives_value, 's-', label="%s" % (name, ))
    ax2.hist(probs_pos, range=(0, 1), bins=10, label=name, histtype="step", lw=2)


ax1.set_ylabel("Fraction of positives")
ax1.set_ylim([-0.05, 1.05])
ax1.legend(loc='lower right')
ax1.set_title("Calibration plots (reliability curve)")

ax2.set_xlabel("Mean predictied value")
ax2.set_ylabel('Count')
ax2.legend(loc='upper center', ncol=2)

plt.tight_layout()
plt.show()


