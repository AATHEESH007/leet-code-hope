# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        c=head
        t=c.next
        e=c.next
        while e and e.next:
            c.next=e.next
            c=c.next
            e.next=c.next
            e=e.next
        c.next=t
        
        return head

        