from pathlib import Path
from datetime import datetime
import argparse

parser = argparse.ArgumentParser(prog='ls', add_help=True, description='list directory contents')
parser.add_argument('path', nargs='?', default='.', help='path help')     # 位置参数,可有可无，缺省值，帮助
parser.add_argument('-l', action='store_true', help='use a long listing format')
parser.add_argument('-a', '--all', action='store_true', help='show all files, do not ignore entries starting with .')
args = parser.parse_args()   # 分析参数，同时传入可迭代的参数
print(args)      # 打印名词空间收集的参数
parser.print_help()

def listdir(path, all=False):
    '''列出本目录文件'''
    p = Path(path)
    for i in p.iterdir():
        if not all and i.name.startswith('.'):  # 不显示隐藏文件
            continue
        yield i.name

# 获取文件类型
def _getfiletype(f:Path):
    if f.is_dir():
        return 'd'
    if f.is_block_device():
        return 'b'
    if f.is_char_device():
        return 'c'
    if f.is_socket():
        return 's'
    if f.is_symlink():
        return 'l'
    else:
        return '-'

def listdirdetail(path, all=False):
    '''详细列出本目录'''
    p = Path(path)
    for i in p.iterdir():
        if not all and i.name.startswith('.'):
            continue
        # mode 硬链接 属主 属组 字节 时间 name
        stat = p.stat()
        t = _getfiletype(p)
        mode = oct(stat.st_mode)[-3:]
        atime = datetime.fromtimestamp(stat.st_atime), strftime('%Y %m %d %H:%M:%S')
        yield (t, mode, stat.st_uid, stat.st_gid, stat.st_size, atime, i.name)

#print(list(listdirdetail(args.path)))
