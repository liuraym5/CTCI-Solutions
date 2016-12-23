class LinkedList:
    def __init__(self, head=None):
        self.head = head;
        self.tail = None;
        self.length = 0
        if head:
            self.length = 1


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        if self.data is None and self.next is None:
            return "[]"
        s = '['
        n = self
        while n.next is not None:
            s += str(n.data) + ', '
            n = n.next
        s += str(n.data) + ']'
        return s

    def append(self, node):
        n = self
        while n.next is not None:
            n = n.next
        if isinstance(node, Node):
            n.next = node
        else:
            n.next = Node(node)
