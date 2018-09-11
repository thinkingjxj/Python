__author__ = 'thinking'

lst = [1,56,7,2]
def sort(iterable,key = lambda a, b: a < b):
    new = []
    for x in iterable:
        for i,y in enumerate(new):
            if key(x,y):
                new.insert(i,x)
                break
        else:
            new.append(x)
    return new

print(sort(lst))
