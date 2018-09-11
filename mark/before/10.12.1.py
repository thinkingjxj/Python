
#def counter():
#    c = [0]
#    def inc():
#        c[0] += 1
#         return c[0]
#    return inc

#foo = counter()
#print(foo(),foo())
#c = 100        # none use
#print(foo())



def counter():
    x = 5
    def inc():
        x += 1     # itself in the local is not assignment
        return x
    return inc

foo = counter()
print(foo(),foo())

