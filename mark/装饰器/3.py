import functools

#def copy_pro(src):
#    def _copy(dst):
#        dst.__name__ = src.__name__
#        dst.__doc__ = src.__doc__
#        return dst
#    return src

def logger(fn):

    def wrapper(*args, **kwargs):
        '''This is a wrapper'''
        print('before')
        x = fn(*args,**kwargs)
        print('end')
        return x
    functools.update_wrapper(wrapper,fn)
    print('{} {}'.format(id(wrapper), id(fn)))
    return wrapper

@logger
def add(x,y):
    '''
    This is a function
    x int
    y int
    '''
    return x + y

print(add.__name__, add.__doc__, add.__qualname__, sep = '\n')
print(id(add.__wrapped__))

print('~'* 30)

import functools

def logger(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        '''This is a wrapper'''
        print('before')
        x = fn(*args,**kwargs)
        print('end')
        return x
    #functools.update_wrapper(wrapper,fn)
    print('{} {}'.format(id(wrapper), id(fn)))
    return wrapper

@logger
def add(x,y):
    '''
    This is a function
    x int
    y int
    '''
    return x + y

print(add.__name__, add.__doc__, add.__qualname__, sep = '\n')
print(id(add.__wrapped__))
