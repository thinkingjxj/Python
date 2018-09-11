# 自己实现base64解码函数

alphabet = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/'

# def base64decode(src:bytes):
#     ret = bytearray()
#     length = len(src)
#     step = 4                  # 每4个
#     for offset in range(0, length, step):
#         tmp = 0x00             # 初始值为0
#         block = src[offset:offset + step]
#         # 开始移位计算
#         for i, c in enumerate(reversed(block)):
#             index = alphabet.find(c)     # find()从左至右查找，找到返回索引，没找到返回-1（好处：不抛异常）
#             if index == -1:
#                 continue
#             tmp += index << i*6          # 移位：左高右低-->大小端(i=0时刚好是最低的6位)
#         ret.extend(tmp.to_bytes(3, 'big'))    # 把3个字符凑出来, extend(iterable_of_ints)将一个可迭代的整数集合追加到当前的bytearray
#     return bytes(ret.rstrip(b'\x00'))      # 把最右边的\x00（ASCII码的零）去掉，不可变
#
# txt = 'TMFu'
# txt = 'TWE='
# txt = 'TwFuTQ=='
# txt = txt.encode()
# print(txt)
# print(base64decode(txt).decode())
#
# # import base64
# # print(base64.b64decode(txt).decode())
#
# def base64(src:bytes):
#     ret = bytearray()
#     length = len(src)
#     step = 4
#     for offset in range(0, length, step):
#         tmp = 0x00
#         block = src[offset: offset + step]
#         for i, c in enumerate(reversed(block)):
#             index = alphabet.find(c)
#             if index == -1:
#                 continue
#             tmp += index << i*6
#     ret.extend(tmp.to_bytes(3, 'big'))
#     return bytes(ret.rstrip(b'\x00'))
#
# txt = 'TPuF'
# txt = txt.encode()
# print(base64decode(txt).decode())




def base64decode(src:bytes):
    ret = bytearray()
    step = 4
    length = len(src)
    for offset in range(0, length, step):
        block = src[offset:offset + step]
        tem = 0x00
        for i, c in enumerate(reversed(block)):
            index = alphabet.find(c)
            if index == -1:
                continue
            tem += index << i*6
        ret.extend(tem.to_bytes(3, 'big'))
    return bytes(ret.rstrip(b'\x00'))

txt = 'TPuF'
print(base64decode(txt.encode()).decode())


# 下面的代码效率更高
def base64decode(src:bytes):
    ret = bytearray()
    step = 4
    length = len(src)
    for offset in range(0, length, step):
        tem = 0x00
        block = src[offset:offset + step]
        for i, c in enumerate(reversed(block)):
            index = alphabet.get(block[-i-1])
            if index is not None:
                tem += index << i*6
            ret.extend(tem.to_bytes(3, 'big'))
    return bytes(ret.rstrip(b'\x00'))






