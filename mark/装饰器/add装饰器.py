# def add(x,y):
#    return x + y

# currying
# def add(x):
#    def _add(y):
#        return x + y
#    return _add

# print(add(4)(6))


def logger(fn):
    def wrapper(*args, **kwargs):
        '''This is a wrapper'''
        print('begin')
        x = fn(*args, **kwargs)
        print('end')
        return x

    return wrapper


@logger
def add(x, y):
    '''This is a function of addition'''
    return x + y


print(add(4, 7))
print(add.__name__, add.__doc__)
