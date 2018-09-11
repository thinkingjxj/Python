def copy_properities(src):
    def _copy(dst):
        dst.__name__ = src.__name__
        dst.__doc__ = src.__doc__
        return dst

    return _copy


def logger(fn):
    @copy_properities(fn)
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


print(add(3, 12))
print(add.__name__, add.__doc__)
