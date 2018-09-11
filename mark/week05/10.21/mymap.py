# 自定义map函数

def mymap(func, *seqs):
    ret = []              # 返回新列表
    for args in zip(*seqs):
        res.append(func(*args))
    return res

def mymap(func, *seqs):
    return [func(*args) for args in zip(*seqs)]

def mymap(func, *seqs):
    res = []
    for args in zip(*seqs):
        yield func(*args)

def mymap(func, *seqs):
    return (func(*args) for args in zip(*seqs))

