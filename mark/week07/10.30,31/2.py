from pathlib import Path
import argparse
from datetime import datetime

parser = argparse.ArgumentParser(prog='ls', add_help=True, description='list directory contents')
parser.add_argument('path', nargs='?', default='.', help='path help')
parser.add_argument('-l', action='store_true', help='list help')
parser.add_argument('-a', '--all', action='store_true', help='help')
args = parser.parse_args()
parser.print_help()


# ls业务功能实现

# 文件列表
def listdir(path, all=False):
    p = Path(path)
    for i in p.iterdir():
        if not all and i.name.startswith('.'):
            continue
        yield i.name
# 获取文件类型
def _getfiletype(f: Path):
    if f.is_dir():
        return 'd'
    elif f.is_symlink():
        return 'l'
    elif f.is_socket():
        return 's'
    elif f.is_char_device():
        return 'c'
    elif f.is_block_device():
        return 'b'
    else:
        return '-'

# 详细列出本目录
def listdirdetail(path, all=False):
    p = Path(path)
    for i in p.iterdir():
        if not all and i.name.startswith('.'):
            continue
        stat = p.stat()
        t = _getfiletype(p)
        mode = oct(stat.st_mode)[-3:]
        atime = datetime.fromtimestamp(stat.st_atime).strftime('%Y-%m-%d %H:%M:%S')
        yield (t, mode, stat.st_uid, stat.st_gid, stat.st_size, atime, i.name)

print(list(listdirdetail(args.path)))
