import random
import re
import datetime
import time
import threading
from queue import Queue
from pathlib import Path

from user_agents import parse


# 数据源
ops = {
    'datetime': lambda timestr: datetime.datetime.strptime(timestr, '%d/%b/%Y:%H:%M:%S %z'),
    'status': int,
    'length': int,
    'request': lambda request: dict(zip(('method', 'url', 'protocol'))),
    'useragent': lambda useragent: parse(useragent)
}

pattern = '''(?P<remote>[\d.]{7,}) - - \[(?P<datetime>[/\w +:]+)\] \
"(?P<method>\w+) (?P<url>\S+) (?P<protocol>[\w/\d.]+)" (?P<statue>\d+) (?P<length>\d+) .+ \
"(?P<useragent>.+)"'''

regex = re.compile(pattern)

def extract(line) ->dict:
    matcher = regex.match(line)
    if matcher:
        return {k:ops.get(k, lambda x: x)(v) for k,v in matcher.groupdict().items()}

def openfile(path:str):
    with open(path) as f:
        for line in f:
            fields = extract(line)
            if fields:
                yield fields
            else:
                continue
def load(*paths):
    '''装载日志文件'''
    for item in paths:
        p = Path(item)
        if not p.exists():
            continue
        if p.is_dir():
            for file in p.iterdir():
                if file.is_file():
                    yield from openfile(str(file))
        elif p.is_file():
            yield from openfile(str(p))

def source():
    while True:
        yield {'value': random.randint(1, 100), 'datetime':datetime.datetime.now()}
        time.sleep(1)

def window(src:Queue, handler, width:int, interval:int):
    """
    窗口函数
    :param src: 数据源，生成器，用来拿数据
    :param handler: 数据除了函数
    :param width: 时间窗口宽度，秒
    :param interval: 处理时间间隔，秒
    """
    start = datetime.datetime.strptime('20170101 00:00:00 +0800', '%Y%m%d %H:%M:%S %z')
    current = datetime.datetime.strptime('20170101 01:00:00 +0800', '%Y%m%d %H:%M:%S %z')
    delta = datetime.timedelta(seconds=current - start)
    buffer = []
    while True:
        # 从数据源取数据
        data = src.get()  # 从队列中取数据，消费者
        if data:
            buffer.append(data)
            current = data['datetime']

        if (current - start).total_seconds() > interval:  # 需要处理数据
            ret = handler(buffer)
            print('{}'.format(ret))
            start = current

        # 重叠部分数据处理
        buffer = [x for x in buffer if x['datetime'] > current - delta]

# 随机数测试处理函数
def handler(iterable):
    vals = [x['value'] for x in iterable]
    return sum(vals) / len(vals)

# 测试
def donothing_handler(iterable):
    return iterable

# 状态码占比
def status_handler(iterable):
    status = {}
    for item in iterable:
        key = item['status']
        if key not in status:
            status[key] = 0
        status[key] += 1
    total = sum(status.values())
    return {k: v/total*100 for k,v in status.items()}
# 浏览器分析
def brower_handler(iterable):
    browers = []
    for item in iterable:
        ua = item['useragent']
        key = (ua.brower.family, ua.brower.version_string)
        browers[key] = browers.get(key, 0) + 1
    return browers

# 调度
def dispatcher(src):
    handlers = []
    queues = []
    # 注册函数
    def reg(handler, width, interval):
        q = Queue
        queues.append(q)
        h = threading.Thread(target=window, args=(q, handler, width, interval))
        handlers.append(h)
    #
    def run():
        for t in handlers:
            t.start()  # 启动线程

        for item in src:
            for q in queues:
                q.put(item)       # 放到队列中，生产者
    return reg, run

if __name__ == "__main__":
    import sys
    path = 'test.log'

    reg, run = dispatcher(load(path))

    reg(status_handler, 10, 5)
    reg(brower_handler, 5, 5)

    run()
