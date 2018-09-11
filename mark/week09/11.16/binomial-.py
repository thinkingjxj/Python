# 二项分布模拟的是在进行整数次独立实验中成功的次数，其中每次实验的成功机会是一定的
# 17世纪的赌场，正对8片币玩法下注，当时流行用9枚硬币来玩。 如果人头朝上的硬币少于5枚，
# 那么我们将输掉一个8分币，否则，我们就赢一个8分币。


import numpy as np
from matplotlib.pyplot import plot, show

cash = np.zeros(10000)
cash[0] = 1000
outcome = np.random.binomial(9, 0.5, size=len(cash))
for i in range(1, len(cash)):
    if outcome[i] < 5:
        cash[i] = cash[i - 1] - 1
    elif outcome[i] < 10:
        cash[i] = cash[i - 1] + 1
    else:
        raise AssertionError('Unexpected outcome' + outcome)

print(outcome.min(), outcome.max())

plot(np.arange(len(cash)), cash)
show()
