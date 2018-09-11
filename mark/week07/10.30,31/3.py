import argparse
import stat
from pathlib import Path
from datetime import datetime


# # 获取目录列表
# def listdir(path, all=False):
#     p = Path(path)
#     for i in p.iterdir():
#         if not all and i.name.startswith('.'):
#             continue
#         yield i.name
# def _getfiletype(f:Path):
#     if f.is_block_device():
#         return 'b'
#     elif f.is_char_device():
#         return 'c'
#     elif f.is_socket():
#         return 's'
#     elif f.is_symlink():
#         return 'l'
#     else:
#         return '-'
# # 获取文件详细信息
# def firedetail(path, all=False):
#     p = Path(path)
#     for i in p.iterdir():
#         if not all and i.name.startswith('.'):
#             continue
#         stat = p.stat()
#         t = _getfiletype(p)
#         mode = oct(stat.st_mode)[-3:]
#         atime = datetime.fromtimestamp(stat.st_atime).strftime('%Y-%m-%d %H:%M:%S')
#         yield (t, mode, stat.st_uid, stat.st_gid, stat.st_size, atime, i.name)
#
# # mode是整数，八进制描述的权限，最终显示为rwx的格式
# modelist = ['r', 'w', 'x', 'r', 'w', 'x', 'r', 'w', 'x']
# def getmodestr(mode:int):
#     m = mode & 0o777
#     mstr = ''
#     for i, v in enumerate(m):
#         if v == 1:
#             mstr += modelist[i]
#         else:
#             mstr += '-'
#
#
#
# def getmodestr(mode:int):
#     m = mode & 0o77
#     mstr = ''
#     for i, v in enumerate(m):
#         if v == 1:
#             mstr += modelist[i]
#         else:
#             mstr += '-'



# 完整代码整合
parser = argparse.ArgumentParser(prog='ls', add_help=False, description='list directory contents')
parser.add_argument('path', nargs='?', default='.', help='path help')
parser.add_argument('-l', action='store_true', help='listing format')
parser.add_argument('-a', '--all', action='store_true', help='show all file names')
parser.add_argument('-h', action='store_true', help='forget')
# args = parser.parse_args()
# parser.print_help()

def listdir(path, all=False, detail=False):
    def _getfiletype(f: Path):
        if f.is_block_device():
            return 'b'
        elif f.is_socket():
            return 's'
        elif f.is_symlink():
            return 'l'
        elif f.is_char_device():
            return 'c'
        else:
            return '-'
    modelist = ['r', 'w', 'x', 'r', 'w', 'x', 'r', 'w', 'x']
    def _getmodestr(mode:int):
        m = mode & 0o77
        mstr = ''
        for i, v in enumerate(m):
            if v == 1:
                mstr += modelist[i]
            else:
                mstr += '-'
        return mstr
    def _listdir(path, all=False, detail=False):
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
                yield (mode, stat.st_uid, stat.st_gid, stat.st_size, atime, i.name)
    # 排序
    yield from sorted(_listdir(path, all, detail), key=lambda x: x[-1])


if __name__ == '__main__':
    args = parser.parse_args()
    print(args)
    parser.print_help()
    files = listdir(args.path, args.all, args.l)
    print(list(files))    # namespace
