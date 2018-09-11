class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __setattr__(self, key, value):
        self.key = value

    def __getitem__(self, item):
        pass

    def __getattribute__(self, item):
        print()

    def __delattr__(self, item):
        print('del')

    def __get__(self, instance, owner):
        pass
