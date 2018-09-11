# import json
#
# d = {'a': 123, 'b':['abc', {'c': 234}], 'd': True, 'e': False, 'f': None}
#
# print(d)
#
# class AA:
#     def ser(self):
#         return 'AA'   # 字符AA
#
#
# print(json.dumps(d))   # 变成了双引号，格式自动转
# print(json.dumps(AA().ser()))


import msgpack
import json

js = '{"person": [{"name": "tom", "age": 18}, {"name": "jerry", "age": 16}, {"name": "ben", "age": 24}], "total": 2}'

d = json.loads(js)
print(d)

msg = msgpack.unpack(d)



