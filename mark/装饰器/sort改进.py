lst = [4, 1, 6, 8, 3, 9, 5]


def sort(iterable, reverse=False):
    new = []
    for x in iterable:
        for i, y in enumerate(new):
            flag = x > y if reverse else x < y
            if flag:
                new.insert(i, x)
                break
        else:
            new.append(x)
    return new

print(1, sort(lst))


def sort(iterable, reverse=False):
    new = []
    for x in iterable:
        for i, y in enumerate(new):
            flag = x > y if not reverse else x < y
            if flag:
                new.insert(i, x)
                break
        else:
            new.append(x)
    return new

print(2, sort(lst))


def sort(iterable, reverse=False):
    def comp(a, b):
        flag = a > b if not reverse else a < b
        return flag

    new = []
    for x in iterable:
        for i, y in enumerate(new):
            if comp(x, y):
                new.insert(i, x)
                break
        else:
            new.append(x)
    return new


def sort(iterable, reverse=False):
    def comp(a, b):
        return a > b if not reverse else a < b

    new = []
    for x in iterable:
        for i, y in enumerate(new):
            if comp(x, y):
                new.insert(i, x)
                break
        else:
            new.append(x)
    return new


def comp(a, b, reverse=False):
    return a > b if not reverse else a < b

def sort(iterable):
    new = []
    for x in iterable:
        for i, y in enumerate(new):
            if comp(x, y, reverse=False):
                new.insert(i, x)
                break
        else:
            new.append(x)
    return new

def comp(a, b):
    return a > b


def sort(iterable, key=comp, reverse=False):
    new = []
    for x in iterable:
        for i, y in enumerate(new):
            if comp(x, y):
                new.insert(i, x)
                break
        else:
            new.append(x)
    return new


def sort(iterable, key=lambda a, b: a < b, reverse=False):
    new = []
    for x in iterable:
        for i, y in enumerate(new):
            if key(x, y):
                new.insert(i, x)
                break
        else:
            new.append(x)
    return new
