class A:
    pass


print(bool(A()))  # True
print(bool(A))  # True  继承自object，object默认有bool


class B:
    def __bool__(self):
        return False


print(bool(B))  # True
print(bool(B()))  # False   实例的


class C:
    def __len__(self):
        return 0


print(bool(C))  # True
print(bool(C()))  # False

# __bool__, 内建函数bool()，或者对象放在逻辑表达式的位置，调用这个函数返回布尔值
# 没有定义__bool__()，就找__len__()返回长度，非0为真。如果__len__()也没有定义，那么所有实例都返回真
