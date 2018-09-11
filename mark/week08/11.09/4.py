import json

d = {'name': 'tom', 'age': 20, 'interest': ['music', 'movie']}
j = json.dumps(d)   # 编码
print(j)

d1 = json.loads(j)   # 解码
print(d1)

# dumps json编码
# dump json编码并存入文件
# loads json解码
# load json解码，从文件读取数据
# 一般json编码的数据很少落地，数据都是通过网络传输，传输的时候，要考虑压缩它
# 本质上来说它就是个文本，就是个字符串
# json很简单，几乎语言编程都支持json，所以应用范围十分广泛
