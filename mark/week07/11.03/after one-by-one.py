import datetime
import re

logline = '''183.60.212.153 - - [19/Feb/2013:10:23:29 +0800] \
"GET /o2o/media.html?menu=3 HTTP/1.1" 200 16691 "-" \
"Mozilla/5.0 (compatible; EasouSpider; +http://www.easou.com/search/spider.html)"'''
ops = {
    'datetime': lambda timestr: datetime.datetime.strptime(timestr, '%Y/%m/%d %H:%M:%S %z'),
    'status': int,
    'length': int,
    'request': lambda request: dict(zip(('method', 'url', 'protocol'), request.split()))
}

pattern = '''
(?P<remote>[\d.]{7,}) - - \[(?P<datetime>[\w/: +]+)\]
\"(?P<method>[\w/ ?=.]+) (?P<url>\d+) (?P<protocol>\d+)\" .+ \"(?P<useragent>[\w/:+. ();]+)\"'''



regex = re.compile(pattern)  # 编译
def extract(line):
    matcher = regex.match(line)
    if matcher:
        return {k: ops.get(k, lambda x: x)(v) for k, v in matcher.groupdict().items()}


print(extract(logline))





# 数据载入
# 对于本项目来说，数据就是日志的一行行记录，载入数据就是文件IO的读取
# 将获取数据的方法封装成函数

def load(path):
    '''装载日志文件'''
    with open(path) as f:
        for line in f:
            fileds = extract(line)
            if fileds:
                yield fileds
            else:
                continue  # TODO 解析失败就抛异常，或者打印日志

# 时间窗口分析
# 很多数据，例如日志，都是和时间相关的，都是按照时间顺序产生的
# 产生数据分析的时候，要按照时间求值
# interval表示每一次求值的时间间隔
# width表示时间窗口宽度，指的是一次求值的时间窗口宽度
# 当width > interval时：
#                数据求值会有重叠
# 当width = interval时：
#                数据求值没有重叠
# 而width < interval一般不采纳这种方案，会有数据缺失

# 时序数据：
# 运维环境中，日志、监控等产生的数据都是与时间相关的数据，
# 按照时间的先后产生并记录下来的数据，所以一般按照时间按对数据进行分析

# 数据分析基本程序结构
# 无限的生成随机数函数，产生时间相关的数据，返回 时间+随机数
# 每次取3个数据，求平均值

# import random
# import datetime
# import time
#
# def source():
#     while True:
#         yield {'value': random.randint(1, 100), 'datetime': datetime.datetime.now()}
#         time.sleep(1)
#
# # 获取数据：3个
# s = source()  # 函数调用
# items = [next(s) for _ in range(3)]
#
# # 处理函数:每次取3个数据，求平均值
# def handler(iterable):
#     vals = [x['value'] for x in iterable]
#     return sum(vals) / len(vals)
#
# print(items)
# print('{:.2f}'.format(handler(items)))

# 上面代码模拟了，一段时间按内产生的数据，等了一段固定时间取数据来计算平均值

# 窗口函数实现
# 将上面的获取数据的程序扩展为window函数，使用重叠的方案

import random
import datetime
import time

def source():
    while True:
        yield {'values': random.randint(1,100), 'datetime': datetime.datetime.now()}
        time.sleep(1)

def window(src, handler, width:int, interval:int):
    '''
    窗口函数
    :param src: 数据源、生成器、用来拿数据
    :param handler: 数据处理函数
    :param width: 时间窗口宽度，秒
    :param interval: 处理时间间隔
    '''
    start = datetime.datetime.strptime('20170101 00:00:00 +0800', '%Y%m%d %H:%M:%S %z')
    current = datetime.datetime.strptime('20170101 01:00:00 +0800', '%Y%m%d %H:%M:%S %z')
    buffer = []   # 窗口中的待计算数据
    delta = datetime.timedelta(seconds=width - interval)
    while True:
        # 从数据源获取数据
        data = next(src)
        if data:   # 存入临时缓冲等待计算
            buffer.append(data)
            current = data['datetime']

        if (current - start).total_seconds() >= interval:
            ret = handler(buffer)
            print('{:.2f'.format(ret))
            start = current

            buffer = [x for x in buffer if x['datetime'] > current]


# 处理函数
def handler(iterable):
    vals = [x['value'] for x in iterable]
    return sum(vals) / len(vals)

window(source(), handler, 10, 5)
