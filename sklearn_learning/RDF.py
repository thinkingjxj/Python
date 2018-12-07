import matplotlib.pyplot as plt
from collections import OrderedDict
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier


random_state = 123
X, y = make_classification(n_samples=500, n_features=25, n_clusters_per_class=1,
                           n_informative=15, random_state=random_state)

ensemble_clfs = [
    ("RandomForestClassifier, max_features='sqrt'",
     RandomForestClassifier(warm_start=True, oob_score=True, max_features='sqrt', random_state=random_state)),
    ("RandomForestClassifier, max_features='log2'",
     RandomForestClassifier(warm_start=True, max_features='log2', oob_score=True, random_state=random_state)),
    ("RandomForestClassifier, max_features=None",
     RandomForestClassifier(warm_start=True, max_features=None, oob_score=True, random_state=random_state))
]

# map a classifier name to a list of (n_estimators, error_rate) pairs
error_rate = OrderedDict((label, []) for label, _ in ensemble_clfs)

min_estimators = 15
max_estimators = 175

for label, clf in ensemble_clfs:
    for i in range(min_estimators, max_estimators+1):
        clf.set_params(n_estimators=i)
        clf.fit(X, y)

        # record the OOB error for each 'n_estimators=i' setting
        oob_error = 1 - clf.oob_score_
        error_rate[label].append((i, oob_error))


# Generate the 'OOB error rate' vs. 'n_estimators' plot
for label, clf_err in error_rate.items():
    xs, ys = zip(*clf_err)
    plt.plot(xs, ys, label=label)


plt.xlim(min_estimators, max_estimators)
plt.xlabel('n_estimators')
plt.ylabel('OOB error rate')
plt.legend(loc='upper right')
plt.show()


























