import re
import datetime

logline = '''183.60.212.153 - - [19/Feb/2013:10:23:29 +0800] \
"GET /o2o/media.html?menu=3 HTTP/1.1" 200 16691 "-" \
"Mozilla/5.0 (compatible; EasouSpider; +http://www.easou.com/search/spider.html)"'''

pattern = '''(?P<remote>[\d.]{7,}) - - \[(?P<datetime>[^\[\]]+)\] "(?P<request>[^"]+)" (?P<status>\d+) (?P<size>\d+) "-" "(?P<useragent>[^"]+)"'''
regex = re.compile(pattern)

def extract(line) -> dict:
    matcher = regex.match(line)
    return {k: ops.get(k, lambda x: x)(v) for k, v in extract(logline).items()}
    #return matcher.groupdict()  # 与37，38行对应

# lambda timestr: datetime.datetime.strptime(timestr, '%d/%b/%Y:%H:%M:%S %z')
# def convert_time(timestr):
#     fmtstr = '%d/%b/%Y:%H:%M:%S %z'
#     dt = datetime.datetime.strptime(timestr, fmtstr)
#     return dt

# lambda request: dict(zip(('method', 'url', 'protocol'), request.split()))
# def convert_request(request: str):
#     return dict(zip(('method', 'url', 'protocol'), request.split()))

ops = {
    'datetime': lambda timestr: datetime.datetime.strptime(timestr, '%d/%b/%Y:%H:%M:%S %z'),
    'status': int,
    'size': int,
    'request': lambda request: dict(zip(('method', 'url', 'protocol'), request.split()))
}

# d = {}
# for k, v in extract(logline).items():
#     d[k] = ops.get(k, lambda x: x)(v)

# d = {k: ops.get(k, lambda x: x)(v) for k, v in extract(logline).items()}
# print(d)

# 日志：
# 生产中会生成大量的系统日志，应用程序日志、安全日志等等
# 分两大类，一种是文件类的，又叫离线文件；另一种在线处理，实时处理，海量处理数据
# 一般采集流程：
# 日志产出、采集（logstash、Flume、Scribe）、存储、分析shu、存储（数据库、NoSQL）
# 开源实时日志分析ELK平台
# logstash收集日志，并存放到ElasticSearch集群中，Kibana则从ES集群查询数据生成图片，返回浏览器端
# 采集（多级、落地（离线日志分析））






