__author__ = 'thinking'


lst = [4,7,32,9,1]
def sort(iterable, key = lambda a,b: a < b, reverse = False):
    new = []
    for x in iterable:
        for i,y in enumerate(new):
            flag = key(x,y) if not reverse else key(y,x)
            if flag:
                new.insert(i,x)
                break
        else:
            new.append(x)
    return new

print(sort(lst))



def sort(iterable, key = None):
    new = []
    if key is None:
        key = lambda a,b: a > b
    for x in iterable:
        for i,y in enumerate(new):
            if key(x,y):
                new.insert(i,x)
                break
        else:
            new.append(x)
    return new