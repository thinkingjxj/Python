logline = '''183.60.212.153 - - [19/Feb/2013:10:23:29 +0800] \
"GET /o2o/media.html?menu=3 HTTP/1.1" 200 16691 "-" \
"Mozilla/5.0 (compatible; EasouSpider; +http://www.easou.com/search/spider.html)"'''

fileds = []
flag = False
tmp = ''
for filed in logline.split():
    if not flag and filed.startswith('[') or filed.startswith('"'):
        if filed.endswith(']') or filed.endswith('"'):
            fileds.append(filed.strip('[]"'))
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
            tmp += ' ' + filed
        continue
    fileds.append(filed)

print(fileds)


# fileds中的数据是有类型的，例如时间、状态码等。对不同的field要做不同的类型转换，甚至是自定义的转换
# 时间转换
# 19/Feb/2013:10:23:29 +800 对应的格式是：%d/%b/%Y:%H:%M:%S %z
# 使用的函数是datetime类的strptime方法

import datetime

def convert_time(timestr):
    return datetime.datetime.strptime(timestr, '%d/%b/%Y:%H:%M:%S %z')

# 可以得到：
lambda timestr: datetime.datetime.strptime(timestr, '%d/%b/%Y:%H:%M:%S %z')

# 状态码和字节数都是整型，使用int函数转换
# 请求信息的解析：
# GET /o2o/media.html?menu=3 HTTP/1.1
# method url protocol三部分都非常重要

def get_request(request:str):
    return dict(zip(['method', 'url', 'protocol'], request.split()))

lambda request: dict(zip(['method', 'url', 'protocol'], request.split()))

# 映射
# 对每一字段命名，然后与值和类型转换的方法对应。解析每一行是有顺序的














