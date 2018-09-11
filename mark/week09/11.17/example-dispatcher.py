class Dispatcher:
    def __init__(self):
        pass

    def reg(self):
        pass

    def run(self):
        while True:
            cmd = input('Please input a commond: ')
            if cmd.strip() == 'quit':
                break
            getattr(self, cmd, lambda: print('Unkown Command {}'.format(cmd)))()



