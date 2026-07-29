"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if head is None:
            return None

        curr = head

        while curr:
            cHead = Node(curr.val)
            cHead.next = curr.random
            curr.random = cHead
            curr = curr.next

        newHead = head.random

        curr = head
        while curr:
            cHead = curr.random
            cHead.random = cHead.next.random if cHead.next else None
            curr = curr.next

        curr = head
        while curr is not None:
            cHead = curr.random
            curr.random = cHead.next
            cHead.next = curr.next.random if curr.next else None
            curr = curr.next

        return newHead