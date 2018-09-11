class Dispatcher:
    def __init__(self):
        self._run()

    def cmd1(self):
        print('cmd1')

    def cmd2(self):
        print('cmd2')

    def _run(self):
        while True:
            cmd = input('Please inout a command: ')
            if cmd.strip() == 'quit':
                break
            getattr(self, cmd, lambda: print('Unkown Command: {}'.format(cmd)))()
            # 使用gerattr方法找到对象的属性的方式，比自己维护一个字典来建立名称和函数之间的关系的方式好多了


Dispatcher()
