from functools import partial


def command_dispatcher():
    cmd_lst = {}

    def reg(cmd, *args, **kwargs):
        def _reg(fn):
            func = partial(fn, *args, **kwargs)
            cmd_lst[cmd] = func
            return func
        return _reg

    def run():
        while True:
            cmd = input('Please input a command: ')
            if cmd.strip() == 'quit':
                break
            cmd_lst.get(cmd, default_func)()

    def default_func():
        print('Unkown command!')
    return reg, run





