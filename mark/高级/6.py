
import datetime

start = datetime.datetime.now()

pre = 0
cur = 1
print(pre, cur, end=' ')


def fib(n, pre=0, cur=1):
    pre, cur = cur, pre + cur
    print(cur, end=' ')
    if n == 2:
        return
    fib(n - 1, pre, cur)


fib(35)

delta = (datetime.datetime.now() - start).total_seconds()
print(delta)
