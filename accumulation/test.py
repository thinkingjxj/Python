import pandas as pd


d = pd.read_excel('C:/Users/thinking/Desktop/t3.xlsx')
print(d.shape)
d = d['PAP_R']
print(d.tail())
print(type(d))

# d = list(d)
# print(type(d))

for k in range(len(d)):
    if k<30:
        d.ix[k] = d.ix[k+1] - d.ix[k]
    # d[-1] = d[-2] - d[-1]
# d = d[:-1]
d = d.iloc[:-1]
# d.columns = ['PAP_R']
print(d)
print(len(d))

# print(d.ix[0])
# print(d.ix[1])
# print(d.ix[1]-d.ix[0])





