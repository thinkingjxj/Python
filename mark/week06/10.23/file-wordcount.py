# 有一个文件，对其进行单词统计，不区分大小写
# 封装成函数->打开->进行单词统计，利用with语法（上下文管理）


# io模块中的类
# 内存中开辟的一个文本模式的buffer，可以像文件对象一样操作它
# 当close方法被调用的时候，这个buffer会被释放

from io import StringIO
# 内存中构建

sio = StringIO()   # 像文件对象一样操作
print(sio.readable(), sio.writable(), sio.seekable())
sio.write('magedu\nPython')
sio.seek(0)
print(sio.readline())
print(sio.getvalue())   # getvalue()获取全部内容，跟文件指针没关系
sio.close()

# StringIO的好处：一般来说，磁盘的操作比内存的操作慢得多，内存足够的情况下，一般的优化思路是少
# 落地，减少磁盘IO的过程，可以大大提高程序的运行效率


# 内存中开辟一个二进制模式的buffer，可以像文件对象一样操作它， 当close方法被调用的时候，这个buffer会被释放

from io import BytesIO

bio = BytesIO()
print(bio.readable(), bio.writable(), bio.seekable())
bio.write(b'magedu\nPython')
bio.seek(0)
print(bio.readline())
print(bio.getvalue())  # 无视指针，输出全部内容
bio.close()

# file-like对象：类文件对象，可以像文件对象一样操作，socket对象、输入输出（stdin、stdout)都是类文件对象
from sys import stdout

f = stdout
print(type(f))
f.write('magedu.com')
