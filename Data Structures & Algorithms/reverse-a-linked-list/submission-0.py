# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        li = []
        while curr:
            li.append(curr.val)
            curr = curr.next
        li = list(reversed(li))
        if not li:
            return None
        newHead = ListNode()
        curr = newHead
        for i in range(len(li)):
            curr.val = li[i]
            if i != len(li)-1:
                curr.next = ListNode()
                curr = curr.next
            else:
                curr.next = None
        return newHead