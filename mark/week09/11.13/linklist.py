class Singlenode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return repr(self.value)


class Linklist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.next = None

    def append(self, value):
        node = Singlenode(value)  # 追加的值
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node  # 修改tail指向

    def iternodes(self):
        current = self.head
        while current:
            yield current
            current = current.next


ll = Linklist()
ll.append(1)
ll.append(8)
ll.append('abc')

ll.append(123)

for x in ll.iternodes():
    print(x)
