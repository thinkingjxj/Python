__author__ = 'thinking'
#x = 5
#def foo():
#    global x
#    x = 10
#    x += 1
#    print(x)
#print(x)
#foo()


def foo():
    global x
    x = 10
    x += 2
    print(x)
    return x    # return None

foo()