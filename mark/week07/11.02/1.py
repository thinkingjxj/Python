import datetime

logline = '''183.60.212.153 - - [19/Feb/2013:10:23:29 +0800] \
"GET /o2o/media.html?menu=3 HTTP/1.1" 200 16691 "-" \
"Mozilla/5.0 (compatible; EasouSpider; +http://www.easou.com/search/spider.html)"'''

names = ('remote', '', '', 'datetime', 'request', 'status', 'length', '', 'useragent')
ops = (None, None, None,
       lambda timestr: datetime.datetime.strptime("19/Feb/2013:10:23:29 +0800", '%d/%b/%Y:%H:%M:%S %z'),
       lambda request: dict(zip(['method', 'url', 'protocol'], request.split())),
       int, int, None, None)

# 提取文本信息
def extract(line):
    fileds = []
    flag = False
    tmp = ''
    for filed in logline.split():
        if not flag and filed.startswith('[') or filed.startswith('"'):
            if filed.endswith(']') or filed.endswith('"'):
                fileds.append(filed.startswith('[]"'))
            else:
                tmp += filed[1:]
                flag = True
            continue
        if flag:
            if filed.endswith(']') or filed.endswith('"'):
                tmp += ' ' + filed[:-1]
                fileds.append(tmp)
                flag = False
                tmp = ''
            else:
                tmp += filed
            continue
        fileds.append(filed)

    info = {}
    for i, filed in enumerate(fileds):
        name = names[i]
        op = ops[i]
        if op:
            info[name] = (op(filed), op)
    return info

print(extract(logline))
