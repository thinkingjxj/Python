# 写一个命令分发器：程序员可以方便的注册函数到某一个命令，用户输入命令时，路由到注册的函数，
# 如果此命令没有对应的注册函数，执行默认函数
# 用户输入用input('>>')
# 分析： 输入命令映射到一个函数，并执行这个函数。应该是cmd_tbl[cmd] = fn的形式，字典正好合适
# 如果输入了一个cmd命令后，没有找到函数，就要调用缺省的函数执行，这正好是字典缺省参数
# cmd是字符串

# 构建全局字典
cmd_tbl = {}
# 注册函数
def reg(cmd, fn):
    cmd_tbl[cmd] = fn
# 缺省函数
def default_func():
    print('Unknown command')
# 调度器
def dispatcher():
    while True:
        cmd = input('>>')
        # 退出条件
        if cmd.strip() == '':
            return
        cmd_tbl.get(cmd, default_func)()

# 自定义函数
def foo1():
    print('magedu')

def foo2():
    print('python')

# 注册函数
reg('mag', foo1)
reg('py', foo2)

# 调度循环
dispatcher()
