import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


d = pd.read_excel('C:/Users/thinking/Desktop/pictus.xlsx')
# print(d)
m,n = d.shape
print(m,n)

plt.figure()
# plt.subplot(431)
plt.plot(range(n), d.iloc[0:1,:].T)

# plt.subplot(432)
plt.plot(range(n), d.iloc[1:2,:].T)

# plt.subplot(433)
plt.plot(range(n), d.iloc[2:3,:].T)

# plt.subplot(434)
plt.plot(range(n), d.iloc[3:4,:].T)

# plt.subplot(435)
plt.plot(range(n), d.iloc[4:5,:].T)

# plt.subplot(436)
plt.plot(range(n), d.iloc[5:6,:].T)

# plt.subplot(437)
plt.plot(range(n), d.iloc[6:7,:].T)

# plt.subplot(438)
plt.plot(range(n), d.iloc[7:8,:].T)

# plt.subplot(439)
plt.plot(range(n), d.iloc[8:9,:].T)

# plt.subplot(4,3,10)
plt.plot(range(n), d.iloc[9:10,:].T)

# plt.tight_layout()    # 调整子图间距

plt.show()
# print(d.iloc[0:1,:])








