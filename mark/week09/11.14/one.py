class Singlenode:
    """代表一个节点"""

    def __init__(self, item, next=None, pre=None):
        self.item = item
        self.next = next
        self.pre = pre

    def __repr__(self):
        return str(self.item)

    def __str__(self):
        return str(self.item)


class Linkedlist:
    """容器类，某种方式存储一个个节点"""

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, item):
        node = Singlenode(item)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node  # 尾巴追加
            node.pre = self.tail  # 前指针指向
        self.tail = node  # 修正自己为尾巴

    def iternodes(self, reverse=False):
        current = self.tail if reverse else self.head
        while current:
            yield current
            current = current.pre if reverse else current.next

    def __getitem__(self, item):
        return self.nodes[item]
