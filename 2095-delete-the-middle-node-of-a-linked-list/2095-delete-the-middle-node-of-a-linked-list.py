# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None : return None
        mid = head
        temp = head
        not_cur = mid
        while not_cur != None and not_cur.next != None:
            temp = mid
            mid = mid.next
            not_cur = not_cur.next.next
        temp.next = mid.next
        return head
