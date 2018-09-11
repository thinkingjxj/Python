__author__ = 'thinking'


# pre = 0
# cur = 1
# print(pre,cur,end=' ')
# n = 4
# for i in range(n-1):
#    pre,cur = cur, pre + cur
#    print(cur,end = ' ')


def fib(n):
    return 1 if n < 2 else fib(n - 1) + fib(n - 2)


for i in range(5):
    print(fib(i), end=' ')
