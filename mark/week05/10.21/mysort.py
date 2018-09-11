#自定义sort函数(降序)

def mysort(iterable):
    ret = []
    for x in iterable:
        for i, y in enumerate(ret):
            if x > y:
                ret.insert(i, x)
                break
        else:
            ret.append(x)

    return ret

print(mysort([1, 8, 5, 39, 4, 6]))


def mysort(iterable, reverse=False):
    ret = []
    for x in iterable:
        for i, y in enumerate(ret):
            flag = x > y if not reverse else x < y
            if flag:
                ret.insert(i, x)
                break
        else:
            ret.append(x)
    return ret
print(mysort([1, 12, 5, 3, 4, 6]))

def mysort(iterable, fn = (lambda a,b: a>b)):
    ret = []
    for x in iterable:
        for i, y in enumerate(ret):
            if fn(x, y):
                ret.insert(i, x)
                break
        else:
            ret.append(x)
    return ret
print(mysort([1, 8, 15, 9, 4, 6]))