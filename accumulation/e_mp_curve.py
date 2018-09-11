import pandas as pd
import matplotlib.pyplot as plt


d = pd.read_excel('C:/Users/thinking/Desktop/e_mp_cur_curve.xlsx')

_, m = d.shape
print(d.head(1))

plt.figure()
for i in range(1, 31):
    plt.plot(range(m), d.iloc[i:i+1,:].T)




plt.grid(True, linestyle = "--", color = "gray")  # 网格
plt.show()





