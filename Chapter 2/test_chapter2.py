import unittest
from chapter2 import *


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

    def test_delMiddleNode(self):
        third = self.head.next.next
        delMiddleNode(third)
        self.assertEqual(str(self.head), "[1, 2, 4, 4, 5]")

    def test_partition(self):
        node = Node(5)
        node.append(4)
        node.append(3)
        node.append(1)
        node.append(4)
        partitioned = partition(node, 4)
        self.assertEqual(str(partitioned), "[3, 1, 5, 4, 4]")

    def test_sum_lists(self):
        first = Node(7)
        first.append(1)
        first.append(6)
        second = Node(5)
        second.append(9)
        second.append(2)
        sum_list = sum_lists(first, second)
        self.assertEqual(str(sum_list), "[2, 1, 9]")
if __name__ == '__main__':
    unittest.main()
