__author__ = 'thinking'
#sorted()

# def sort(iterable, reverse =  False):
    #new = []
    #for x in iterable:

    #    new.append(x)
   # return new

lst = [1,7,4,7,3,9,8]

def sort(iterable):
    new = []
    for x in iterable:
        for i,y in enumerate(new):
            if x > y:
                new.insert(i,x)
                break
        else:
            new.append(x)
    return new

print(sort(lst))



def sort(iterable, reverse = False):
    new = []
    for x in iterable:
        for i,y in enumerate(new):
            flag = x > y if  reverse else x < y
            if flag:
                new.insert(i,x)
        else:
            new.append(x)
    return new

print(sort(lst))