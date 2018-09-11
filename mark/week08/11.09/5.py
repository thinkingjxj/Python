import msgpack

# packb序列化对象，提供了dumps来兼容pickle和json
# unpackb反序列化对象，提供了loads来兼容
# packb序列化对象保存到文件对象，提供了dump来兼容
# unpackb反序列化对象保存到文件对象，提供了load来兼容
d = {'person': [{'name': 'tom', 'age': 18}, {'name': 'jerry', 'age': 16}], 'total': 2}
b = msgpack.packb(d)
print(len(b))
print(b)

d1 = msgpack.unpackb(b)
print(d1)

d1 = msgpack.unpackb(b, encoding='utf-8')
print(d1)


