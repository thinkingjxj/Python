class Animal:
    x = 123
    def __init__(self, name):
        self._name = name
        self.__age = 10
        self.weight = 20



if __name__ == '__main__':
    print("animal Module's name = {}".format(dir()))