def foo(w,u='abc',z=123):
    u = 'xyz'
    z = 789
    print(w,u,z)


print(foo.__defaults__)
#foo()
foo('magedu')
print(foo.__defaults__)
