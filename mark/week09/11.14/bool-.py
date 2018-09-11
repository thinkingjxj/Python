class A:
    pass


print(bool(A()))  # True


class B:
    def __bool__(self):
        return False


print(bool(B))    # True
print(bool(B()))  # False


class C:
    def __len__(self):
        return 0


print(bool(C()))  # False
