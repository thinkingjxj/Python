import pandas as pd
import matplotlib.pyplot as plt
from sklearn.manifold import MDS
import numpy as np


d = np.array([(0, 1046, 608, 1859),
              (1046, 0, 824, 1149),
              (608, 825, 0, 1280),
              (1859, 1149, 1280, 0)])
index = ['beijing', 'shanghai', 'zhengzhou', 'guangzhou']
columns = index

w = pd.DataFrame(d, index, columns)
print(w)

mds = MDS()
mds.fit(d)
a = mds.embedding_
print(a)

plt.scatter(a[0:, 0], a[0:, 1], c='r')
plt.show()