class Animal:
    x = 123

    def __init__(self, name):
        self._name = name
        self.__age = 10
        self.weight = 20

print('animal Modile\'s names = {}'.format(dir()))

