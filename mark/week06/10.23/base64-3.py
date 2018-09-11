# 4变3

alphabet = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/'

def base64decode(src:bytes):
    ret = bytearray()
    step = 4
    for offset in range(0, len(src), step):
        block = src[offset: offset + step]
        tmp = 0x00
        for i, c in enumerate(reversed(block)):
            index = alphabet.find(c)
            if index == -1:
                continue
            tmp += index << i*6
        ret.extend(tmp.to_bytes(3, 'big'))
    return bytes(ret.rstrip(b'\x00'))

txt = 'TFPd'
txt = txt.encode()
print(txt)
# print(base64decode(txt).decode())


