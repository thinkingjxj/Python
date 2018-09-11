__author__ = 'thinking'

import datetime

start = datetime.datetime.now()

n = 35


def fib(n):
    return 1 if n < 2 else fib(n - 1) + fib(n - 2)


for i in range(n):
    print(fib(i), end=' ')

delta = (datetime.datetime.now() - start).total_seconds()
print(delta)
