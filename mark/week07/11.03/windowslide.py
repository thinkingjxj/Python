import datetime
import random
import re
import threading
from queue import Queue
from user_agents import parse



# logline = '''183.60.212.153 - - [19/Feb/2013:10:23:29 +0800] \
# "GET /o2o/media.html?menu=3 HTTP/1.1" 200 16691 "-" \
# "Mozilla/5.0 (compatible; EasouSpider; +http://www.easou.com/search/spider.html)"'''

pattern = '''(?P<remote>[\d.]{7,}) - - \[(?P<datetime>[^\[\]]+)\] "(?P<request>[^"]+)" (?P<status>\d+) (?P<size>\d+) ("-" )?"(?P<useragent>[^"]+)"'''
regex = re.compile(pattern)

def extract(line) -> dict:
    matcher = regex.match(line)
    return {k: ops.get(k, lambda x: x)(v) for k, v in extract(logline).items()}

ops = {
    'datetime': lambda timestr: datetime.datetime.strptime(timestr, '%d/%b/%Y:%H:%M:%S %z'),
    'status': int,
    'size': int,
    'request': lambda request: dict(zip(('method', 'url', 'protocol'), request.split())),
    'useragent': lambda useragent: parse(useragent)
}


def openfile(path:str):
    with open(path) as f:
        for line in f:
            d = extract(line)
            if d:
                yield d
            else:
                continue


def load(*path):
    for file in path:
        p = Path(path)
        if not p.exists():
            continue
        if p.is_dir():
            for x in p.iterdir():
                if x.is_file():
                    yield from openfile(str(x))
        elif p.is_file():
            yield from openfile(str(p))


# 无限生成随机数据：时间+数据
def source():
    while True:
        yield {'value': random.randint(1, 100),
               'datetime': datetime.datetime.strptime('20170101 00:00:00 +0800', '%Y%m%d %H:%M:%S %z')}

# *********************************************************************第一部分数据源，第二部分窗口函数数据源处理，第三部分如何分发数据和调度
# 窗口函数
def window(src:Queue, handler, width: int, interval: int):
    start = datetime.datetime.strptime('20170101 00:00:00 +0800', '%Y%m%d %H:%M:%S %z')
    current = datetime.datetime.strptime('20170101 01:00:00 +0800', '%Y%m%d %H:%M:%S %z')
    buffer = []   # 处理数据
    delta = datetime.timedelta(seconds=width - interval)
    while True:     # 没有数据会阻塞
    #for data in src:    # 队列不能遍历
        data = src.get()     # 分发给消费者，block阻塞，在另一个线程中，阻塞也没事
        if data:
            #data = next(src)
            buffer.append(data)
            current = data['datetime']

        if (current - start).total_seconds() >= interval:
            ret = handler(buffer)   # 处理数据
            print('{:.2f}'.format(ret))
            start = current
            # 重叠部分数据处理
            # buffer的处理
            # tmp = []
            # for i in buffer:
            #      if i['datetime'] > current - delta:
            #           tmp.append(i)
            buffer = [x for x in buffer if x['datetime'] >= current - delta]

def donothing_handler(iterable:list):
    print(iterable)
    return iterable



# 状态码函数
def status_handler(iterable:list):
    d = {}
    for item in iterable:
        key = item['status']
        if key not in d.keys():
            d[key] = 0
        d[key] += 1
    total = sum(d.values())
    return {k:v/total*100 for k, v in d.items()}


# 浏览器分析
def brower_handler(iterable:list):
    for item in iterable:
        ua = item['useragent']
        # ua = parse('')
        return ua.browser.family, ua.browser.version_string

##################################################


# # 函数处理：求平均值
# def handler(iterable):
#     vals = [x['value'] for x in iterable]
#     return sum(vals) / len(vals)
#
# # 函数调用
# # window(load('test.log'), donothing_handler, 10, 5)
#
#
# def size_handler(iterable: list):
#     # TODO
#     pass
# 分发器
def dispatcher(src):
    # 队列列表
    queues = []
    threads = []    # 注册完就消失了，所以放到列表里
    def reg(handler, width, interval):
        q = Queue()
        queues.append(q)     # 注册一个就写一个
        #window(q, handler, width, interval)
        t = threading.Thread(target=window, args=(q, handler, width, interval))
        threads.append(t)
        pass
    def run():
        for t in threads:
            t.start()

        for x in src:   # src是生成器，x是字典，window函数处理queue中的字典
            for q in queues:   # 消费者的，window，put
                q.put(x)


    return reg, run

reg, run = dispatcher(load('test.log'))

# reg注册  窗口
reg(donothing_handler, 10, 5)

reg(status_handler, 10, 5)

# 启动
run()
