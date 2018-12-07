import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from sklearn import clone
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier

# parameters
n_classes = 3
n_estimators = 30
cmap = plt.cm.RdYlBu
plot_step = 0.02  # fine step width for decision surface contours
plot_step_coarser = 0.5  # step widths for coarse classifier guesses
Random_seed = 13   # fix the seed on each iteration

iris = load_iris()

plot_idx = 1

models = [DecisionTreeClassifier(max_depth=None),
          RandomForestClassifier(n_estimators=n_estimators),
          ExtraTreesClassifier(n_estimators==n_estimators),
          AdaBoostClassifier(DecisionTreeClassifier(max_depth=3), n_estimators=n_estimators)]


for pair in ([0, 1], [0, 2], [2, 3]):
    for model in models:
        x = iris.data[: pair]
        y = iris.target

        # shuffle
        idx = np.arange(x.shape[0])
        np.random.seed(Random_seed)
        np.random.shuffle(idx)
        x = x[idx]
        y = y[idx]

        # standardize
        mean = x.mean(axis=0)
        std = x.std(axis=0)
        x = (x - mean) / std

        # train
        clf = clone(model)
        clf = model.fit(x, y)

        scores = clf.score(x, y)



















