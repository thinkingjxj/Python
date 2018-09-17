
import pymysql
from pandas.core.frame import DataFrame
import datetime
import time
import pandas as pd

conn = pymysql.connect(host="192.168.99.19",
                       user="energy_prolicy",
                       password="energy_prolicy",
                       database="energy_prolicy"
                       )
# 使用cursor()方法创建游标
cursor = conn.cursor()

data = pd.read_sql_query("select  time,U1,U2,U3,U4,U5,U6,U7,U8,U9,U10  from yuenergy", conn)
# print(data.U1)

data = data.drop([12, 19, 56, 57, 58])
# data = data.dropna(axis=0, how='any')

data = data.reset_index(drop=True)
# data=data.drop('time',axis=1)

data_corr = data.corr().abs()
data_corr = data_corr.U1.sort_values(ascending=False)
print(data_corr)
print(type(data_corr))

corr = list(data_corr)
print(corr)

# 获取时间
now = datetime.datetime.now()
print(type(now))
time = now.strftime("%Y/%m/%d")
print(type(time))

# 将处理好的数据存储到mysql表中
sql = "insert into yucorr(corr) values(%s)"

for i in range(0, 10):
    cursor.execute(sql, corr[i])
    # print(data_corr[i], time, time)

print(int(conn.insert_id()))

cursor.close()
conn.commit()
conn.close()
