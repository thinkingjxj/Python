import random


class Lnode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_  # next_防止与内置的next冲突


# 自定义异常， ValueError为标准异常类
class LinkedListUnderflow(ValueError):
    pass


class LList:
    def __init__(self):  # 初始化空表
        self.head = None

    def is_empty(self):
        return self.head is None

    def prepend(self, elem):  # 前端插入
        self.head = Lnode(elem, self.head)

    def pop(self):  # 返回pop值e
        if self.head is None:
            raise LinkedListUnderflow('in pop')
        e = self.head.elem
        self.head = self.head.next  # 指向下一个
        return e

    def append(self, elem):  # 后端插入
        if self.head is None:
            self.head = Lnode(elem, self.head)
            return
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Lnode(elem)

    def pop_last(self):
        if self.head is None:
            raise LinkedListUnderflow('in pop_last')
        p = self.head
        if p.next is None:  # 表中只有一个元素
            self.head = None
            e = p.elem
            return e
        while p.next.next is not None:  # 直到p.next是最后一个
            p = p.next
        e = p.next.elem
        p.next = None
        self.tail = p
        return e

    def filter(self, pred):  # 筛选生成器
        p = self.head
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p = p.next


mlist1 = LList()
mlist1.prepend(99)
for i in range(11, 20):
    mlist1.append(random.randint(1, 20))

print(mlist1)

for x in mlist1.filter(lambda y: y % 2 == 0):
    print(x)
