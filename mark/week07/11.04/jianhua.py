import re
import datetime
import time
import random
from queue import Queue
from pathlib import Path
import threading
from user_agents import parse

# 183.69.210.164 - - [07/Apr/2017:09:32:53 +0800] "GET /app/include/authcode.inc.php HTTP/1.1" 200 384
# "http://job.magedu.com/index.php?m=login" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36
# (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"


ops = {
    'datetime': lambda timestr: datetime.datetime.strptime(timestr, '%d/%b/%Y:%H:%M:%S %z'),
    'status': int,
    'length': int,
    'request': lambda request: dict(zip(('method', 'url', 'protocol'), request.split())),
    'useragent': lambda useragent: parse(useragent)
}

pattern = '''(?P<remote>[\d.]{7,}) - - \[(?P<datetime>[/\w +:]+)\] \
"(?P<method>\w+) (?P<url>[/\w.]+) (?P<protocol>[/\w.]+)" (?P<status>\d+) (?P<length>\d+) .+ \
"(?P<useragent>.*)"'''
regex = re.compile(pattern)
def extract(line) ->dict:
    matcher = regex.match(line)
    if matcher:
        return {k: ops.get(k, lambda x: x)(v) for k, v in matcher.groupdict().items()}


def openfile(path:str):
    with open(path) as f:
        for line in f:
            d = extract(line)
            if d:
                yield d
            else:
                continue

def load(*paths):
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
        return {'values': random.randint(1, 100), 'datetime': datetime.datetime.now()}
    time.sleep(1)

def window(src:Queue, handler, width:int, interval:int):
    start = datetime.datetime.strptime('20170101 00:00:00 +0800', '%Y%m%d %H:%M:%S %z')
    current = datetime.datetime.strptime('20170101 01:00:00 +0800', '%Y:%m:%d %H:%M:%S %z')
    delta = datetime.timedelta(seconds=width-interval)
    buffer = []
    while True:
        # 从队列中获取数据，消费者
        data = src.get()
        if data:
            buffer.append(data)
            current = data['datetime']

        if (current - start).total_seconds() > interval:
            ret = handler(buffer)
            print('{}'.format(ret))
            start = current

            # 重叠数据处理
            buffer = [x for x in buffer if x['datetime'] > current - delta]

# 随机数测试
def handler(iterable):
    vals = [x['values'] for x in iterable]
    return sum(vals) / len(vals)

# 状态占比
def status_handler(iterable):
    status = {}
    for item in iterable:
        key = item['status']
        if key not in status:
            status[key] = 0
        status[key] += 1
    total = sum(status.values())
    return {k: v/total*100 for k, v in status.items()}

# 浏览器函数处理
def browers_handler(iterable):
    browers = {}
    for item in iterable:
        ua = item['useragent']
        key = (ua.brower.family, ua.brower.version_string)
        browers[key] = browers.get(key, 0) + 1
    return browers

def dispather(src):
    handlers = []
    queues = []
    def reg(handler, width, interval):
        q = Queue()
        queues.append(q)

        h = threading.Thread(target=window, args=(q, handler, width, interval))
        handlers.append(h)

    def run():
        for t in handlers:
            t.start()

        for item in src:
            for q in queues:
                q.put(item)

    return reg, run

reg, run = dispather(load('paths'))

if __name__ == '__main__':
    import sys
    path = 'test.log'

    reg(status_handler, 10, 5)
    reg(browers_handler, 5, 5)
    run()
