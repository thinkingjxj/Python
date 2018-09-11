import re
import datetime
import time
from pathlib import Path

logline = '''183.60.212.153 - - [19/Feb/2013:10:23:29 +0800] \
"GET /o2o/media.html?menu=3 HTTP/1.1" 200 16691 "-" \
"Mozilla/5.0 (compatible; EasouSpider; +http://www.easou.com/search/spider.html)"'''

pattern = '''(?P<remote>[\d.]{7,}) - - \[(?P<datetime>[^\[\]]+)\] "(?P<request>[^"]+)" (?P<status>\d+) (?P<size>\d+) .* "(?P<useragent>[^"]+)"'''
regex = re.compile(pattern)

def extract(line) -> dict:
    matcher = regex.match(line)
    return {k: ops.get(k, lambda x: x)(v) for k, v in extract(logline).items()}

ops = {
    'datetime': lambda timestr: datetime.datetime.strptime(timestr, '%d/%b/%Y:%H:%M:%S %z'),
    'status': int,
    'size': int,
    'request': lambda request: dict(zip(('method', 'url', 'protocol'), request.split()))
}

def load(path:str):
    '''单文件装载'''
    with open('C:/\\Users\\10649\\Python\\11.04\\test.log') as f:
        for line in f:
            fields = extract(line)
            if fields:
                yield fields
            else:
                continue  # TODO 不合格数据有多少











