import pandas as pd


d = pd.read_excel('E:/data.xlsx')
m,n = d.shape

a = sorted([d.iloc[0].corr(d.iloc[i]) for i in range(m)], reverse=True)
# print(a)
a = [d.iloc[0].corr(d.iloc[i]) for i in range(m)]
# print(a)


# print(d.iloc[:, 0:1])
# print(d.iloc[:, 1:2])
# print(d[['计量', '通讯']])
print(d['计量'].corr(d['通讯']))

# print(d[['计量']].corr(d[['通讯']]))
# e = d.iloc[0:3]
# cr = d.iloc[1:2,1:]

# print(e)
# print(cr)
