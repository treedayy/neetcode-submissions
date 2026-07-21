# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        prev = None
        curr = second

        while curr: 
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        final = ListNode()
        curr = final
        first = head
        binary_count = 0
        while first and prev:
            if binary_count == 0:
                curr.next = first
                first = first.next
                binary_count = 1
            else:
                curr.next = prev
                prev = prev.next
                binary_count = 0
            curr = curr.next

        if first is not None:
            curr.next = first


        
