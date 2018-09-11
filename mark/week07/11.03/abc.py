
import re
import datetime

logline = ''''''

pattern = ''''''

regex = re.compile(pattern)

def extract(line):
    matcher = regex.match(line)
    if matcher:
        return {k:ops.get(k, lambda x:x)(v) for k, v in matcher.groupdict().items()}
ops = {
    'datetime': lambda timestr:datetime.datetime.strptime(timestr, "%d/%b/%Y:%H:%M:%S %z"),
    'status': int,
    'size': int,
    'request': lambda request:dict(zip(('method', 'url', 'protocol'), request.split()))
}

# line = []  # 模拟读取文件
# for line in lines:
#     d = extract(line)
#     if d:
#         pass
#     else:         # 不合格数据有多少
#         continue













