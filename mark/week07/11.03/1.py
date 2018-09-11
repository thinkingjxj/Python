import datetime
import random

def source():
    while True:
        yield datetime.datetime.now(), random.randint(1, 100)

src = source()
def window(src, handler, width:int, interval:int):
    start = datetime.datetime.strptime('timestr', '%d/%b/%Y:%H:%M:%S %z')


lst = []
# lst = [next(src) for _ in range(3]
lst.append(next(src))
lst.append(next(src))
lst.append(next(src))
sum(lst) // len(lst)

# 1
# def handler(iterable):   # 处理函数
#     return sum(lst) // len(lst)

# 2
# def handler(iterable):   # 处理函数
#     lst = [next(src) for _ in range(3)]
#     return sum(lst) // len(lst)


