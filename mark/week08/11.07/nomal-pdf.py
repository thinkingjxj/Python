import numpy as np
import matplotlib.pyplot as plt

N = 10000
nomal_values = np.random.normal(size=N)
dummy, bins, dummy1 = plt.hist(nomal_values, np.sqrt(N), normed=True, lw=1)
sigma = 1
mu = 0
plt.plot(bins, 1/(sigma*np.sqrt(2*np.pi)) * np.exp(-(bins - mu) ** 2 / (2 * sigma**2)), lw=2)
plt.show()
