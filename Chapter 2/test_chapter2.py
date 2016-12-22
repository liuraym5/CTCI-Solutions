import unittest
from chapter2 import *


class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        if self.next is None:
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
        n.next = node


class Chapter2Tests(unittest.TestCase):
    def setUp(self):
        self.head = Node(1)
        self.head.append(Node(2))
        self.head.append(Node(3))
        self.head.append(Node(4))
        self.head.append(Node(4))
        self.head.append(Node(5))

    def test_removeDups(self):
        removeDups(self.head)
        self.assertEqual(str(self.head), "[1, 2, 3, 4, 5]")

    def test_kthToLast(self):
        self.assertEqual(kthToLast(self.head, 4).data, 3)
if __name__ == '__main__':
    unittest.main()
