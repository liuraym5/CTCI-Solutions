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

    def test_is_palindrome(self):
        self.assertFalse(is_palindrome(self.head))
        n = Node("h")
        n.append("a")
        n.append("n")
        n.append("n")
        n.append("a")
        n.append("h")
        self.assertTrue(is_palindrome(n))

    def test_is_intersecting(self):
        head1 = Node("3")
        i = Node("9")
        i.append("10")
        head1.append(i)
        self.head.append(i)
        self.assertTrue(is_intersecting(head1, self.head))

    def test_is_circular(self):
        n = Node("3")
        c = Node("2")
        n.append(c)
        n.append("1")
        n.append(c)
        self.assertEqual(is_circular(self.head), self.head)
        self.assertEqual(is_circular(n), c)
if __name__ == '__main__':
    unittest.main()
