# 链表在内存中是有序的
# 列表中放的是链表节点的地址，更高效


class SingleNode:
    def __init__(self, item, next=None,pre = None):
        self.item = item
        self.next = next
        self.pre = pre

    def __repr__(self):
        return str(self.item)

    def __str__(self):
        return str(self.item)


class Linklist:
    def __init__(self):
        self.notes = []  # 不需要插入的列表，检索方便，但是插入，remove不合适
        self.head = None
        self.tail = None

    def append(self, item):
        node = SingleNode(item)
        #pre = self.tail
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.notes.append(node)
        self.tail = node

    def iternotes(self):
        current = self.head
        while current:
            yield current
        current = current.next

# 凡是有索引，便于查询，比如列表
# 增删改
