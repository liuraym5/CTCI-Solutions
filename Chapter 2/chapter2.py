from collections import *
from LinkedList import LinkedList, Node

# 2.1: Remove Dups
# O(n)
def removeDups(head):
    s = set();
    node = head;
    while node.next != None:
        s.add(node.data)
        if node.next.data in s:
            node.next = node.next.next
        node = node.next


# 2.2: Return Kth to Last node
# O(n)
def kthToLast(head, k):
    length = 1
    n = head
    while n.next != None:
        n = n.next
        length += 1
    position = length - k
    if k <= length:
        n = head
        while position > 0:
            n = n.next
            position -= 1
        return n
    return None


# 2.3: Delete Middle Node
# O(1)
def delMiddleNode(node):
    node.data = node.next.data
    node.next = node.next.next


# 2.4: Partition
# O(n)
def partition(node, value):
    firsthalf, secondhalf = None, None
    while node is not None:
        # build two partitions
        if node.data < value:
            if not firsthalf:
                firsthalf = Node()
                startfirst = firsthalf
            else:
                firsthalf.next = Node()
                firsthalf = firsthalf.next
            firsthalf.data = node.data
        else:
            if not secondhalf:
                secondhalf = Node()
                startsecond = secondhalf
            else:
                secondhalf.next = Node()
                secondhalf = secondhalf.next
            secondhalf.data = node.data
        node = node.next
    # join second partition to the end of the first partition
    firsthalf.next = startsecond
    return startfirst


# 2.5: Sum Lists
# O(n)
def sum_lists(head1, head2):
    multiplier = 1
    num1, num2 = 0, 0
    r_list = None
    while head1 is not None:
        num1 += head1.data * multiplier
        multiplier *= 10
        head1 = head1.next
    multiplier = 1
    while head2 is not None:
        num2 += head2.data * multiplier
        multiplier *= 10
        head2 = head2.next
    sum_string = str(num1 + num2)
    for ch in reversed(sum_string):
        if r_list is None:
            r_list = Node(int(ch))
        else:
            r_list.append(int(ch))
    return r_list


# 2.6: Palindrome
# O(n)
def is_palindrome(head):
    count = 0
    stack = deque()
    n = head
    while n is not None:
        stack.append(n.data)
        n = n.next
        count += 1
    n = head
    count = count // 2
    while count > 0:
        if stack.pop() != n.data:
            return False
        n = n.next
        count -= 1
    return True

# 2.7: Intersection
# O(n)
def is_intersecting(head1, head2):
    s1 = set()
    s2 = set()
    n = head1
    while n is not None:
        s1.add(n)
        n = n.next
    n = head2
    while n is not None:
        s2.add(n)
        n = n.next
    if s1.isdisjoint(s2):
        return False
    return True


# 2.8: Loop Detection
# O(n)
def is_circular(head):
    s = set()
    n = head
    while n is not None:
        if n in s:
            return n
        s.add(n)
        n = n.next
    return head
