def copy_pro(src):
    def wrapper(*args, **kwargs):
        print('before')
        x = src(*args, **kwargs)
        print('after')
        return x

    return wrapper


@copy_pro
def copy_properties(src, dst):
    dst.__name__ = src.__name__
    dst.__doc__ = src.__doc__
    dst.__qualname__ = src.__qualname__


# currying
def copy_pro(src):
    def _copy(dst):
        dst.__name__ = src.__name__
        dst.__doc__ = src.__doc__
        dst.__qualname__ = src.__qualname__
        return dst

    return _copy
