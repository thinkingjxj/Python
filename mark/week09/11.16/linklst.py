import random


class Lnode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self, elem):
        self._head = Lnode(elem, self._head)

    def pop(self):
        if self._head is None:
            raise Exception('Error')
        e = self._head.elem
        self._head = self._head.next
        return e

    def append(self, elem):
        if self._head is None:
            self._head = Lnode(elem, self._head)
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = Lnode(elem)

    def pop_last(self, elem):
        if self._head is None:
            raise Exception
        p = self._head
        if p.next is None:  # 只有一个元素
            e = p.elem
            p.next = None
            return e
        while p.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    def filter(self, pred):
        p = self._head
        while p is not None:
            yield p.elem
        p = p.next

    def printall(self):
        p = self._head
        while p is not None:
            print(p.elem, end='')
            if p.next is not None:
                print(', ', end='')
            p = p.next
        print('')


class Linklist(LList):
    def __init__(self):
        self._head = None
        self._rear = None

    def prepend(self, elem):

        if self._head is None:  # 空表
            self._head = Lnode(elem, self._head)
            self._rear = self._head
        else:
            self._head = Lnode(elem, self._head)

    def append(self, elem):
        if self._head is None:  # 空表
            self._head = Lnode(elem, self._head)
            self._rear = self._head
        else:
            self._rear.next = Lnode(elem)
            self._rear = self._rear.next

    def pop_last(self, elem):
        if self._head is None:  # 空表
            raise Exception
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        self._rear = p
        return e


mlist = Linklist()
mlist.append(99)
for i in range(11, 20):
    mlist.append(random.randint(1, 20))

print(mlist)
print(mlist.printall())
