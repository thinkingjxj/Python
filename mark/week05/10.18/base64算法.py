alphabet = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/'
teststr = 'abcd'

def base64(src):
    ret = bytearray()
    length = len(src)
    r = 0
    for offset in range(0, length, 3):
        if offset + 3 <= length:
            triple = src[offset: offset + 3]
        else:
            triple = src[offset:]
            r = 3 - len(triple)
            triple = triple + '\x00'
        b = int.from_bytes(triple.encode(), 'big')
        print(hex(b))
        for i in range(18, -1, -6):
            if i == 18:
                index = b >> i
            else:
                index = b >> i & 0x3F
            ret.append(alphabet[index])
        for i in range(1, r + 1):
            ret[-i] = 0x3D
    return ret


print(base64(teststr))

print('~' * 30)
import base64

print(base64.b64encode(teststr.encode()))
