import re
import datetime

logline = '''183.60.212.153 - - [19/Feb/2013:10:23:29 +0800] \
"GET /o2o/media.html?menu=3 HTTP/1.1" 200 16691 "-" \
"Mozilla/5.0 (compatible; EasouSpider; +http://www.easou.com/search/spider.html)"'''

def extract(line) -> dict:
    pattern = '''(?P<remote>[\d.]{7,}) - - \[(?P<datetime>[^\[\]]+)\] "(?P<request>[^"]+)" (?P<status>\d+) (?P<size>\d+) "-" "(?P<useragent>[^"]+)"'''    # 放内部不太好
    regex = re.compile(pattern)   # 放内部不太好
    matcher = regex.match(line)
    return matcher.groupdict()

ops = {
    'datetime': lambda timestr: datetime.datetime.strptime(timestr, '%d/%b/%Y:%H:%M:%S %z'),
    'status': int,
    'size': int,
    'request': lambda request: dict(zip(('method', 'url', 'protocol'), request.split()))
}

# d = {k: ops.get(k, lambda x: x)(v) for k, v in extract(logline).items()}
# print(d)

# 进一步简化：21行内容可以放到第12行，即：

pattern = '''(?P<remote>[\d.]{7,}) - - \[(?P<datetime>[^\[\]]+)\] "(?P<request>[^"]+)" (?P<status>\d+) (?P<size>\d+) "-" "(?P<useragent>[^"]+)"'''
regex = re.compile(pattern)
def extract(line) -> dict:
    matcher = regex.match(line)
    return {k: ops.get(k, lambda x: x)(v) for k, v in extract(logline).items()}

# 字典默认为None，考虑到此中情形，继续完善
def extract(line) -> dict:
    matcher = regex.match(line)
    if matcher:
        return {k: ops.get(k, lambda x: x)(v) for k, v in extract(logline).items()}
# 外部调用
lines = []
for line in lines:
    d = extract(line)
    if d:
        pass
# 或者
def extract(line) -> dict:
    matcher = regex.match(line)
    if matcher:
        return {k: ops.get(k, lambda x: x)(v) for k, v in extract(logline).items()}
    else:
        raise Exception('No match')

# 异常处理：try，except
lines = []
for line in lines:
    try:
        d = extract(line)
    except:
        pass


lines = []
for line in lines:
    d = extract(line)
    if d:
        pass
    else:
        # 不合格数据有多少
        pass


# lines = []
# for line in lines:
#     d = extract(line)
#     if d:
#         pass
#     else:
#         # 不合格数据有多少
#         pass










