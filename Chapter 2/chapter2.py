from collections import *

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