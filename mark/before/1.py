
def counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

foo = counter()
foo()
foo()
