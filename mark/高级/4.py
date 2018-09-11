
import datetime

start = datetime.datetime.now()

pre = 0
cur = 1
print(pre, cur, end=' ')

n = 35
for i in range(n-1):
    pre, cur = cur, pre + cur
    print(cur, end=' ')

delta = (datetime.datetime.now() - start).total_seconds()
print(delta)


