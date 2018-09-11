def mymap(func, *seqs):
    res = []
    for args in zip(*seqs):
        res.append(func(*args))
    return res


def mymap(func, *seqs):
    return [func(*args) for args in zip(*seqs)]


def mymap(func, *seqs):
    res = []
    for args in zip(*seqs):
        res.append(func(*args))
        yield func(*args)


def mymap(func, *seqs):
    return (func(*args) for args in zip(*seqs))
