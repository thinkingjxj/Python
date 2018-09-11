# import argparse


# parser = argparse.ArgumentParser()  # 获得一个参数解析器
# args = parser.parse_args()       # 分析参数
# parser.print_help()              # 打印帮助

# argparse不仅仅做了参数的定义和解析，还自动帮助生成了帮助信息。
# 尤其是usage，可以看到现在定义的参数是否是自己想要的
# 解析器的参数
# prog程序的名字，缺省使用sys.argv[0]
# add_help自动为解析器增加-h和--help选项，默认为True
# description为程序功能添加描述

# parser = argparse.ArgumentParser(prog='ls', add_help=True, description='list directory contents')
# parser.print_help()

# 位置参数解析
# ls基本功能应该解决目录内容的打印，打印的时候应该指定目录路径，需要位置参数。

# parser = argparse.ArgumentParser(prog='ls',add_help=True, description='list directory contents')
# parser.add_argument('path')
#
# args = parser.parse_args()  # 分析参数
# parser.print_help()         # 打印帮助
# 会出错：ls:error: the following arguments are required:path
# 程序等定义为：
# ls[-h] path
# -h为帮助，可有可无
# path为位置参数，必须提供

# 传参
# parse_args(args=None, namespace=None)
# args参数列表，一个可迭代对象。内部会把可迭代对象转换成list。
# 如果为None则使用命令行传入参数，非None则使用args参数的可迭代对象

# parser = argparse.ArgumentParser(prog='ls', add_help=True, description='list directory contents')
# parser.add_argument('path')  # 位置参数
#
# args = parser.parse_args(('/etc',))   # 分析参数，同时传入可迭代的参数
# print(args)   # 打印名词空间中收集的参数
# parser.print_help()   # 打印帮助

# 获得一个参数解析器
# parser = argparse.ArgumentParser(prog='ls', add_help=True, description='list directory contents')
# parser.add_argument('path', nargs='?', default='.', help='path help')  # 位置参数、可有可无、缺省值、帮助信息
#
# args = parser.parse_args()   # 分析参数，同时传入可迭代的参数
# print(args)
# parser.print_help()

# 可以看出path也变成可选的，没有提供就使用默认值， 表示当前路径
# help表示帮助文档中这个参数的描述
# nargs表示这个参数接收结果参数， ?表示可有可无
# default表示如果不提供该参数，就使用这个值

# parser = argparse.ArgumentParser(prog='ls', add_help=True, description='list directory contents')
# parser.add_argument('path', nargs='?', default='.', help='directory')
# parser.add_argument('-l', action='store_true', help='use a long listint format')
# parser.add_argument('-a', '--all', action='store_true', help='show all files, do not ignore entries starting with .')
# args = parser.parse_args()
# print(args)
# parser.print_help()

# 到目前为止，已经解决了参数的定义和传参的问题，下面就要解决业务问题：
# 1. 列出所有指定路径的文件，默认是不递归的
# 2. -a显示所有文件，包括隐藏文件
# 3. -l详细列表模式显示


import argparse
from pathlib import Path
from datetime import datetime

parser = argparse.ArgumentParser(prog='ls', add_help=True, description='list directory contents')
parser.add_argument('path', nargs='?', default='.', help='directory')
parser.add_argument('-l', action='store_true', help='use a long listing format')
parser.add_argument('-a', '--all', action='store_true', help='show all files, do not ignore entries starting with .')

args = parser.parse_args()
print(args)
parser.print_help()

def listdir(path, all=False):
    '''列出本目录文件'''
    p = Path(path)
    for i in p.iterdir():
        if not all and i.name.startswith('.'):
            continue
        yield i.name

print(list(listdir(args.path)))

# 获取文件类型
def _getfiletype(f:Path):
    if f.is_dir():
        return 'd'
    elif f.is_block_device():
        return 'c'
    elif f.is_socket():
        return 's'
    elif f.is_symlink():
        return 'l'
    else:
        return '-'

# -rw-rw-r-- 1 python python 5 Oct 25 00:07 test4
def listdir(path, all=False):
    p = Path(path)
    for i in p.iterdir():
        if not all and i.name.startswith('.'):
            continue
        # mode 硬链接 属主 属组 字节 时间 name
        start = p.stat()
        t = _getfiletype(p)
        mode = oct(stat.st_mode)[-3:]
        atime = datetime.fromtimestamp(stat.st_atime).strftime('%Y-%m-%d %H:%M:%S')
        yield (t, mode, stat.st_uid, stat.st_gid, start.st_size, atime, i.name)

print(list(listdirdetail(args.path)))
