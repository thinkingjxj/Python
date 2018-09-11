
def foo(xyz=[]):
    xyz.append(1)
    print(xyz)

foo()
foo()

# print(xyz)    # NameError
# �鿴foo.__defaults__
print(foo.__defaults__ )
