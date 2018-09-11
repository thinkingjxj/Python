
import argparse
import stat
from pathlib import Path
from datetime import datetime

parser = argparse.ArgumentParser(prog='ls', add_help=False, description='list directory contents')
parser.add_argument('path', nargs='?', default='.', help='path help')
parser.add_argument('-l', action='store_true', help='use a long listing format')
parser.add_argument('-a', '--all', action='store_true', help='show all files, do not ignore entries startwith .')
parser.add_argument('-h', '--human-readable', action='store_true', help='with -l, print sizes in human readable format')

def listdir(path, all=False, detail=False, human=False):
    def _getfiletype(f: Path):
        if f.is_block_device():
            return 'b'
        elif f.is_char_device():
            return 'c'
        elif f.is_socket():
            return 's'
        elif f.is_symlink():
            return 'l'
        else:
            return '-'
    modelist = ['r', 'w', 'x', 'r', 'w', 'x', 'r', 'w', 'x']
    def _getmodestr(mode:int):
        m = mode & 0o77
        mstr = ''
        for i,v in enumerate(m):
            if v == 1:
                mstr += modelist[i]
            else:
                mstr += '-'
        return mstr
    def _gethuman(size:int):
        units = ['', 'K', 'M', 'G', 'T', 'P']
        depth = 0
        while size >= 1000:
            size = size // 1000
            depth += 1
        return '{}{}'.format(size, units[depth])
    def _listdir(path, all=False, detail=False, human= False):
        p = Path(path)
        for i in p.iterdir():
            if not all and i.name.startswith('.'):
                continue
            if not detail:
                yield (i.name,)
            else:
                stat = i.stat()
                mode = _getfiletype(p) + _getmodestr(stat.st_mode)
                atime = datetime.fromtimestamp(stat.st_atime).strftime('%Y-%m-%d %H:%M:%S')
                size = str(stat.st_size) if not human else _gethuman(stat.st_size)
                yield (mode, stat.st_uid, stat.st_gid, stat.st_size, atime, i.name)

    yield from sorted(_listdir(path, all, detail, human), key=lambda x: x[-1])   # 根据文件名进行排序

if __name__ == '__main__':
    args = parser.parse_args()
    print(args)
    parser.print_help()
    file = listdir(args.path, args.l, args.human_readable)
    print(list(file))





# modelist = ['r','w','x','r','w','x','r','w','x']
# def _getmodestr(mode:int):
#     m = mode & 0o777
#     print(mode)
#     print(m, bin(m))
#     mstr = ''
#     for i, v in enumerate(bin(m)):
#         if v == '1':
#             mstr += modelist[i]
#         else:
#             mstr += '-'
#     return mstr
#
# print(_getmodestr(700))
#
# # 增加一个函数，能够解决单位转换
# def _gethuman(size:int):
#     units = ['', 'K', 'M', 'G', 'T', 'P']
#     depth = 0
#     while size >= 1000:
#         size = size // 1000
#         depth += 1
#     return '{}{}'.format(size, units[depth])

