class Singlenode:
    """代表一个节点"""
    def __init__(self, item, next=None, pre=None):
        self.item = item
        self.next = next
        self.pre = pre

    def __repr__(self):
        return str(self.item)


class Linkedlist:
    """容器类，某种方式存储一个个节点"""

    def __init__(self):
        self.nodes = []
        self.head = None
        self.tail = None

    def __len__(self):
        return len(self.nodes)

    def append(self, item):
        node = Singlenode(item)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.nodes.append(node)
        self.tail = node

    def iternodes(self, reverse=False):
        current = self.head
        while current:
            yield current
            current = current.next

    def __getitem__(self, item):
        return self.nodes[item]


ll = Linkedlist()
node = Singlenode(5)
ll.append(node)
node = Singlenode(7)
ll.append(node)
ll.append(3)

for node in ll.iternodes():
    print(node)

print(ll[0], ll[1], ll[2])

