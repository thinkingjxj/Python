# 循环单链表类
class Lnode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LCList:  # 循环单链表类
    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

    def prepend(self, elem):
        p = Lnode(elem)
        if self._rear is None:
            p.next = p  # 建立一个结点的环
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p

    def append(self, elem):
        self.prepend(elem)
        self._rear = self._rear.next

    def pop(self):  # 前端弹出
        if self._rear is None:
            raise Exception
        p = self._rear.next  # 头
        if self._rear is p:  # 空
            self._rear = None
        else:
            self._rear.next = p.next
        return p.elem

    def printall(self):
        if self.is_empty():
            return
        p = self._rear.next
        while True:
            print(p.elem)
            if p is self._rear:
                break
            p = p.next
