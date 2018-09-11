# node: elem + next_  (next_防止与内置next冲突)
class Lnode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


llist1 = Lnode(1)
b = llist1
for i in range(2, 11):
    b.next = Lnode(i)
    b = b.next

b = llist1
while b is not None:
    print(b.elem)
    b = b.next


# 自定义异常
class LinkedListUnderflow(ValueError):
    pass


# llist类的定义，初始化函数和简单操作
class LList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def prepend(self, elem):  # head
        self.head = Lnode(elem, self.head)

    def append(self, elem):
        if self.head is None:
            self.head = Lnode(elem)
            return  # why return?
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Lnode(elem)

    def pop(self, elem):  # 返回pop出的值，末尾pop
        if self.head is None:
            raise LinkedListUnderflow('in pop')
        e = self.head.elem
        self.head = self.head.next
        return e

    def pop_last(self, elem):
        if self.head is None:
            raise LinkedListUnderflow
        p = self.head
        if p.next is None:  # 表中只有一个元素
            e = p.elem
            self.head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    def find(self, pred):
        p = self.head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p = p.next
