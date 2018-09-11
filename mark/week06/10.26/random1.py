
from io import BytesIO, StringIO

bio = BytesIO()
print(bio.readable(), bio.writable(), bio.seekable())
bio.write(b'magede\nPython')
bio.seek(0)
print(bio.readline())
print(bio.getvalue())
bio.close()

sio = StringIO()
print(sio.readable(), sio.writable(), sio.seekable())
sio.write('magedu\nPython')
sio.seek(0)
print(sio.readline())
print(sio.getvalue())
sio.close()

# 二者都是io模块中的类：在内存中，开辟一个文本或者二进制模式的buffer，可以像文件对象一样操作它，
# 当close方法被调用的时候，这个buffer会被释放
# getvalue()获取全部内容，跟文件指针没有关系
# StringIO的好处：一般来说，磁盘的操作比内存的操作要慢的多，内存足够的情况下，
# 一般的优化思路是少落地，减少磁盘IO的过程，可以大大提高程序的运行效率


# 类文件对象：file-like对象，可以像文件对象一样操作
from sys import stdout

f = stdout
print(type(f))
f.write('magedu.com')  # 控制台输出
