import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA



def test_stationarity(timeseries):
    rolmean = pd.Series.rolling(timeseries, window=12).mean()  # 对size个数据进行移动平均
    rol_weighted_mean = pd.Series.ewm(timeseries, span=12).mean()  # 对size个数据进行加权移动平均
    rolstd = pd.Series.rolling(timeseries, window=12).std()    # 偏离原始值多少
    # 画出起伏统计
    orig = plt.plot(timeseries, color='blue', label='Original')
    mean = plt.plot(rolmean, color='red', label='Rolling Mean')
    weighted_mean = plt.plot(rol_weighted_mean, color='green', label='weighted Mwan')
    std = plt.plot(rolstd, color='black', label='Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Debilation')
    plt.show(block=False)
    # 进行df测试
    print('Result of Dickry-Fuller test')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#lags used', 'Number of observations used'])
    for key, value in dftest[4].items():
        dfoutput['Critical value(%s)' % key] = value
    print(dfoutput)



dta = pd.read_excel('C:/Users/thinking/Desktop/t3.xlsx')
print(dta.shape)
t = dta.copy()
ts = dta['PAP_R']

for k in range(len(dta)):
    if k<30:
        ts.ix[k] = ts.ix[k+1] - ts.ix[k]
# estimationg
# ts = dta.iloc[:-1]['PAP_R']
ts = ts.iloc[:-1]
# print('ts: ', ts.tail())
# print(ts.shape)
# plt.subplot(211)
plt.plot(ts)
plt.legend(loc='best')
plt.show()

# test_stationarity(ts)
# plt.show()

# print(ts.tail())
# plt.subplot(212)
# ts = np.log(ts)
# plt.plot(ts)
 # plt.show()

moving_avg = pd.Series.rolling(ts, 12).mean()
# plt.plot(moving_avg, color='red')
# plt.show()

ts_moving_avg_diff = ts - moving_avg
# print(ts_moving_avg_diff)
ts_moving_avg_diff.dropna(inplace=True)
# test_stationarity(ts_moving_avg_diff)
# plt.show()
# plt.savefig('p1')

# 时间序列的差分
ts_diff = ts.diff(1)
plt.plot(ts_diff)
plt.legend(loc='best')
plt.show()
ts_diff.dropna(inplace=True)
# test_stationarity(ts_diff)
# plt.show()
# 上图看出一阶差分大致已经具有周期性，不妨绘制二阶差分对比
ts_diff1 = ts.diff(1)
ts_diff2 = ts_diff1.diff(1)
plt.plot(ts_diff1, label='diff 1')
plt.plot(ts_diff2, label='diff 2')
plt.legend(loc='best')
plt.show()



# 预测  确定参数
lag_acf = acf(ts_diff, nlags=20)
lag_pacf = pacf(ts_diff, nlags=20, method='ols')
# q的获取：ACF图中曲线第一次穿过上置信区间，这里q取2
plt.subplot(121)
plt.plot(lag_acf)
plt.axhline(y=0, linestyle='--', color='gray')
plt.axhline(y=-1.96 / np.sqrt(len(ts_diff)), linestyle='--', color='gray')  # lowwer置信区间
plt.axhline(y=1.96 / np.sqrt(len(ts_diff)), linestyle='--', color='gray')   # upper置信区间
plt.title('Autocorrelation Function')
# p获取：PACF图中曲线第一次穿过上置信区间，这里p取2
plt.subplot(122)
plt.plot(lag_pacf)
plt.axhline(y=0, linestyle='--', color='gray')
plt.axhline(y=-1.96 / np.sqrt(len(ts_diff)), linestyle='--', color='gray')
plt.axhline(y=1.96 / np.sqrt(len(ts_diff)), linestyle='--', color='gray')
plt.title('Partial Autocorrelation Function')
plt.tight_layout()   # Automatically adjust subplot parameters to give specified padding.
plt.show()


# AR model
model = ARIMA(ts, order=(2, 1, 0))
result_AR = model.fit(disp=-1)     # no output information is printed
plt.subplot(311)
plt.plot(ts_diff)
plt.plot(result_AR.fittedvalues, color='red')
plt.legend(loc='best')
plt.title('AR model RSS:%.4f' % sum(result_AR.fittedvalues - ts_diff) ** 2)
# print('!!!!!!: ',result_AR.fittedvalues)


# MA Model
model = ARIMA(ts, order=(0, 1, 2))
result_MA = model.fit(disp=-1)
plt.subplot(312)
plt.plot(ts_diff)
plt.plot(result_AR.fittedvalues, color='red')
plt.legend(loc='best')
plt.title('MA model RSS:%.4f' % sum(result_MA.fittedvalues - ts_diff) ** 2)    # 误差平方和



# ARIMA model
model = ARIMA(ts, order=(1, 1, 0))
result_ARIMA = model.fit(disp=-1)
plt.subplot(313)
plt.plot(ts_diff)
plt.plot(result_ARIMA.fittedvalues, color='red')
plt.legend(loc='best')
plt.title('ARIMA RSS:%.4f' % sum(result_ARIMA.fittedvalues - ts_diff) ** 2)
plt.show()

# predictions_ARIMA
predictions_ARIMA_diff = pd.Series(result_ARIMA.fittedvalues, copy=True)
print(predictions_ARIMA_diff.head())   # 发现数据是没有第一行的，因为有1的延迟

predictions_ARIMA_diff_cumsum = predictions_ARIMA_diff.cumsum()
print(predictions_ARIMA_diff_cumsum.head())

predictions_ARIMA_log = pd.Series(ts.ix[0], index=ts.index)
predictions_ARIMA_log = predictions_ARIMA_log.add(predictions_ARIMA_diff_cumsum, fill_value=0)
print(predictions_ARIMA_log.tail())
print(ts.tail())

predictions_ARIMA = predictions_ARIMA_log
plt.plot(ts)
plt.plot(predictions_ARIMA)
plt.legend(loc='best')
plt.title('predictions_ARIMA RMSE: %.4f' % np.sqrt(sum((predictions_ARIMA - ts) ** 2)))
plt.show()


# d = pd.DataFrame({'dta':dta, 'ts':ts, 'predict':predictions_ARIMA_log})
ts = pd.DataFrame(ts)
predictions_ARIMA_log = pd.DataFrame(predictions_ARIMA_log, columns=['predict'])


# print(t.iloc[:-1,1])
# print(predictions_ARIMA_log)
# tmp = pd.DataFrame(np.array(t.iloc[:-1,1]) + np.array(predictions_ARIMA_log))
# print(tmp)


d = pd.concat([t, ts, predictions_ARIMA_log], axis=1)
# print(d.head())
# print(d.iloc[:,2:4])
#
# d.iloc[1:,2:3] = d.iloc[:-1, 2:3]
# d.iloc[1:,3:4] = d.iloc[:-1, 4:4]
# print(d.head())
# print(d.tail())

# print(ts.describe())
# print(predictions_ARIMA_log.describe())



d.to_csv('C:/Users/thinking/Desktop/test1.csv', index=False, sep=',')
