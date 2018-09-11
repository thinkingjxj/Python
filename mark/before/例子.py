
def foo(xyz = [], u = 'abc', z = 123):
    xyz.append(1)
    return xyz
print(foo(),id(foo))
print(foo.__defaults__)
print(foo(),id(foo))
print(foo.__defaults__)
