
class A:
    def __init__(self):
        self.a = 'a'
        self.b = 'b'

    def __hash__(self):
        return  1

    def __eq__(self, other):
        return self.a == other.a

print(hash(A()))
print(A(), A())
s = {A(), A()}
print(s)        # 有__eq__语句才去重
