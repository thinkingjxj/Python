# 完善命令分发器：
# 要求函数可以带参数（不考虑可变参数、keyword-only参数)
# 用户输入命令，执行相应的函数

# 自定义函数可以有任意参数，可变参数、keyword-only除外
from functools import partial


def command_dispatcher():
    cmd_tbl = {}  # 构建全局字典

    def reg(cmd, *args, **kwargs):  # 注册函数
        def _reg(fn):
            func = partial(fn, *args, **kwargs)
            cmd_tbl[cmd] = func
            return func

        return _reg

    def default_func():  # 构建缺省函数
        print('Unknown command')

    def dispatcher():  # 构建调度器  或者run()
        while True:
            cmd = input('Please input cmd>>')
            if cmd.strip() == '':
                return
            cmd_tbl.get(cmd, default_func)()

    return reg, dispatcher  # 元组


reg, dispatcher = command_dispatcher()  # 解构


# 自定义函数
@reg('mag', 200, 300, 100)
def foo1(x, y, z):
    print('magedu', x, y, z)


@reg('py', 300, b=400)
def foo2(a, b=100):
    print('Python', a, b)


dispatcher()
