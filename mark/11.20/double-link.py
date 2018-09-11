# 作业：将前面的链表封装成容器
# 要求：
# 1. 提供__getitem__、__iter__、__setitem__方法
# 使用一个列表辅助完成上面的方法
# 3. 进阶：不使用列表，完成上面的方法


class SingleNode:
    def __init__(self, elem, pre=None, next=None):
        self.elem = elem
        self.pre = pre
        self.next = next

    def __repr__(self):
        return repr(self.elem)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.items = []

    def append(self, elem):
        node = SingleNode(elem)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node  # AttributeError: 'NoneType' object has no attribute 'next'
            node.pre = self.tail
        self.tail = node
        self.items.append(node)


    def iternotes(self, reverse=False):
        current = self.tail if reverse else self.head
        while current:
            yield current
            current = current.pre if reverse else current.next

    def insert(self, index, elem):
        if index < 0:
            raise ValueError('Wrong index {}'.format(index))
        current = None
        if current is None:  # head头结点
            self.append(elem)
            return
        node = SingleNode(elem)
        for i, node in enumerate(self.iternotes()):
            if i == index:
                current = node
                break
        pre = current.pre
        if pre is None:         # head处
            self.head = node
            node.pre = pre
        node.next = current
        current.pre = node
        node.pre = pre
        pre.next = node
        self.items.insert(index, elem)

    def pop(self):
        if self.tail is None:
            raise Exception('Empty')
        node = self.tail
        elem = node.elem
        pre = node.pre
        if pre is None:  # node is head
            self.head = None
            self.tail = None
        else:
            pre.next = None
            self.tail = None
        return elem

    def remove(self, index):
        if self.head is None:
            raise Exception('Empty')
        if index < 0:
            raise ValueError('Wrong index {}'.format(index))
        current = None
        # if current is None:
        #     raise ValueError('Wrong index {}'.format(index))
        for i, node in enumerate(self.iternotes()):
            if i == index:
                current = node
                break
        pre = current.pre
        next = current.next
        if pre is None and next is None:  # only one node
            self.head = None
            self.tail = None
        elif pre is None:
            self.head = next
            next.pre = None
        elif next is None:
            self.tail = pre
            pre.next = None
        else:
            pre.next = next
            next.pre = pre
        del current


ll = LinkedList()
ll.append('abc')
for i in range(1, 6):
    ll.append(i)
print(1, ll)
ll.append('def')
print(2, ll.head, ll.tail)

for x in ll.iternotes(True):
    print(x)
print('=' * 35)
ll.remove(3)
ll.remove(5)
ll.remove(0)
ll.remove(1)
for x in ll.iternotes():
    print(x)

print('*' * 35)
ll.insert(3, 7)
ll.insert(20, 'ae')
ll.insert(1, 2)
ll.insert(0, 'abcd')
for x in ll.iternotes():
    print(x)
