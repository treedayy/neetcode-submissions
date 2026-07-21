# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        n_c = 1
        final = ListNode()
        c = final
        while prev:
            if n_c != n:
                c.next = prev
                c = c.next
            prev = prev.next
            n_c+=1
        c.next = None
        prev2 = None
        curr2 = final.next
        while curr2:
            next_node = curr2.next
            curr2.next = prev2
            prev2 = curr2
            curr2 = next_node
        
        return prev2

        
