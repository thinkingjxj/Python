# from __future__ import print_function
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot

dta = [10930, 10318, 10595, 10972, 7706, 6756, 9092, 10551, 9722, 10913, 11151, 8186, 6422,
       6337, 11649, 11652, 10310, 12043, 7937, 6476, 9662, 9570, 9981, 9331, 9449, 6773, 6304, 9355,
       10477, 10148, 10395, 11261, 8713, 7299, 10424, 10795, 11069, 11602, 11427, 9095, 7707, 10767,
       12136, 12812, 12006, 12528, 10329, 7818, 11719, 11683, 12603, 11495, 13670, 11337, 10232,
       13261, 13230, 15535, 16837, 19598, 14823, 11622, 19391, 18177, 19994, 14723, 15694, 13248,
       9543, 12872, 13101, 15053, 12619, 13749, 10228, 9725, 14729, 12518, 14564, 15085, 14722,
       11999, 9390, 13481, 14795, 15845, 15271, 14686, 11054, 10395]

# dta = np.array(dta, dtype=np.float)
dta = pd.Series(dta)
dta.index = pd.Index(sm.tsa.datetools.dates_from_range('2001', '2090'))
# dta.plot()
#
# fig = plt.figure()
# ax1 = fig.add_subplot(111)
# diff1 = dta.diff(1)
# diff1.plot(ax=ax1)
#
# fig = plt.figure()
# ax2 = fig.add_subplot(111)
# diff2 = dta.diff(2)
# diff2.plot(ax=ax2)
# plt.show()

# diff1 = dta.diff(1)
# fig = plt.figure(figsize=(12, 8))
# ax1 = fig.add_subplot(211)
# fig = sm.graphics.tsa.plot_acf(dta, lags=40, ax=ax1)  # lags表示滞后的阶数
# ax2 = fig.add_subplot(212)
# fig = sm.graphics.tsa.plot_pacf(dta, lags=40, ax=ax2)
#
# plt.show()


# arma_mod20 = sm.tsa.ARMA(dta, (7, 0)).fit()
# print(arma_mod20.aic, arma_mod20.bic, arma_mod20.hqic)
# arma_mod30 = sm.tsa.ARMA(dta, (0, 1)).fit()
# print(arma_mod30.aic, arma_mod30.bic, arma_mod30.hqic)
# arma_mod40 = sm.tsa.ARMA(dta, (7, 1)).fit()
# print(arma_mod40.aic, arma_mod40.bic, arma_mod40.hqic)
arma_mod50 = sm.tsa.ARMA(dta, (8, 0)).fit()
# print(arma_mod50.aic, arma_mod50.bic, arma_mod50.hqic)


# # 检验残差序列
resid = arma_mod50.resid
# fig = plt.figure(figsize=(12, 8))
# ax1 = fig.add_subplot(211)
# ax1 = sm.graphics.tsa.plot_acf(resid.values.squeeze(), lags=40, ax=ax1)
# ax2 = fig.add_subplot(212)
# fig = sm.graphics.tsa.plot_pacf(resid, lags=40, ax=ax2)
# plt.show()
# 残差的ACF和PACF图，可以看到序列残差基本为白噪声


# print(sm.stats.durbin_watson(arma_mod50.resid.values))  # 2.023164481786418
# 所以残差序列不存在自相关性
# DW检验：0<=DW<=4; DW=4 <=> p=-1 即存在负自相关性；DW=2 <=> p=0 即不存在（一阶）自相关性

print(stats.normaltest(resid))
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)
fig = qqplot(resid, line='q', ax=ax, fit=True)
plt.show()
