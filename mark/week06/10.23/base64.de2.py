# 提高效率的地方: 1. reversed可以不需要  2. alphabet.find效率低

from collections import OrderedDict
base_tb1 = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/'
alphabet = OrderedDict(zip(base_tb1, range(64)))

def base64decode(src:bytes):
    ret = bytearray()
    length = len(src)

    step = 4
    for offset in range(0, length, step):
        tmp = 0x00                            # 16进制的0
        block = src[offset:offset + step]

        for i in range(4):
            index = alphabet.get(block[-i-1])      # get：key不存在，返回缺省值，没有设置缺省值，返回None
            if index is not None:                  # A的索引为0
                tmp += index << i*6
        ret.extend(tmp.to_bytes(3, 'big'))      # extend(iterable_of_ints)将一个可迭代的整数集合追加到当前bytearray
    return bytes(ret.rstrip(b'\x00'))      # 二进制的0

txt = 'TwFu'
txt = txt.encode()
print(txt)
print(base64decode(txt).decode())

