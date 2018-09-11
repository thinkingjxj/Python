def foo(x=[],u = 'abc', z = 123):
    x = x[:]
    x.append(1)
    print(x)

foo()
print(foo.__defaults__)
foo()
print(foo.__defaults__)
foo([10])
print(foo.__defaults__)
foo([10,5])
print(foo.__defaults__)