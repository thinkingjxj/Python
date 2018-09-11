# 双向链表
class Singlenode:
    def __init__(self, item, pre=None, next=None):
        self.item = item
        self.pre = pre
        self.next = next

    def __repr__(self):
        return repr(self.item)


class LinkedList:
    def __init__(self): # 初始化空链表
        self.head = None
        self.tail = None

    def append(self, item):  # 追加：1.节点 2. 追加
        node = Singlenode(item)
        # 空表append，非空append
        if self.tail is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node



    def insert(self, index, item):
        node = Singlenode(item)
        # 表头插入、表中表尾插入一个道理
        if index < 0:
            raise ValueError('Wrong Index {}'.format(index))
        current = None
        if current is None:
            self.append(item)  # 链表为空直接追加
            return
        for i, node in enumerate(self.iternodes()):
            if i == index:
                current = node
                break
        # 找到了
        node = Singlenode(item)
        pre = current.pre
        if pre is None:  # head node
            self.head = node
        else:
            pre.next = node  # 前->node
            node.pre = pre  # node->后
        node.next = current
        current.pre = node

    def pop(self):  # 尾部pop
        if self.tail is None:
            raise Exception('Empty')
        node = self.tail
        item = node.item
        pre = node.pre
        if pre is None:  # node is head
            self.head = None
            self.tail = None
        else:
            pre.next = None
            self.tail = None
        return item

    def remove(self, index):
        if self.tail is None:
            raise Exception('Empty')
        if index < 0:
            raise ValueError('Wrong Index {}'.format(index))
        current = None
        if current is None:
            raise ValueError('Wrong Index {}. Out of bound'.format(index))
        for i, node in enumerate(self.iternodes()):
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

    def iternodes(self, reverse=False):
        current = self.tail if reverse else self.head
        while current:
            yield current
            current = current.pre if reverse else current.next


ll = LinkedList()
ll.append('abc')
# for i in range(1, 6):
#     ll.append(i)
ll.append(1)
ll.append(2)
ll.append('def')
print(ll.head, ll.tail)
# print(ll)
for x in ll.iternodes():
    print(x)

