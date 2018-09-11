
class SingleNode:
    def __init__(self, item, pre=None, next=None):
        self.item = item
        self.next = next
        self.pre = pre
    def __repr__(self):
        return repr(self.item)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.items = []

    def append(self, item):
        node = SingleNode(item)
        if self.head is None:
            self.head = node
        else:
            self.tail = node
            node.pre = self.tail
        self.tail = node
        self.items.append(node)

    def insert(self, index, item):
        if index < 0:
            raise ValueError('Wrong Index {}'.format(index))
        current = None
        for i, node in enumerate(self.iternodes()):
            if i == index:
                current = node
                break
        if current is None:
            self.append(item)
            return
        node = SingleNode(item)
        pre = current.pre
        if pre is None:
            self.head = node
        else:
            pre.next = node
            node.pre = pre
        node.next = current
        current.pre = node
    #    self.items.insert(index) = node

    def iternodes(self, reverse=False):
        current = self.tail if reverse else self.head
        while current:
            yield current
            current = current.pre if reverse else current.next






