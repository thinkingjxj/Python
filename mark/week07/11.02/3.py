import datetime
import re

logline = '''183.60.212.153 - - [19/Feb/2013:10:23:29 +0800] \
"GET /o2o/media.html?menu=3 HTTP/1.1" 200 16691 "-" \
"Mozilla/5.0 (compatible; EasouSpider; +http://www.easou.com/search/spider.html)"'''

# names = ('remote', 'datetime', 'method', 'url', 'protocol', 'status', 'length', 'useragent')

# ops = (None, lambda timestr: datetime.datetime.strftime(timestr, '%d/%b/%Y:%H:%M:%S %z'),
#        None, None, None, int, int, None)

# 进一步改造：利用命名分组，ops也就可以和名词对应了，names就没有必要存在了
pattern = '''
(?P<remote>[\d.]{7,}) - - \[(?P<datetime>[\w/: +]+)\]
\"(?P<method>[\w/ ?=.]+) (?P<url>\d+) (?P<protocol>\d+)\" .+ \"(?P<useragent>[\w/:+. ();]+))\"
'''

regex = re.compile(pattern)

def extract(line):
    matcher = regex.match(line)
    if matcher:
        return {k: ops.get(k, lambda x: x)(v) for k, v in matcher.groupdict().items()}

ops = {
    'datetime': (lambda timestr: datetime.datetime.strptime(timestr, "%d/%b/%Y:%H:%M:%S %z")),
    'status': int,
    'length': int,
    'request': lambda request: dict(zip(('method', 'url', 'protocol'), request.split()))
}

print(extract(logline))

