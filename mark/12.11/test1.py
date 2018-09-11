print('this is test1 module')

class A:
    def showmodule(self):
        print('{}.a = {}'.format(self.__module__, self))
        print(self.__class__.__name__)


a = A()
a.showmodule()

