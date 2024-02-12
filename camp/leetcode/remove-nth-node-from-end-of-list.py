# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prior = head
        i = 0
        while i < n:
            if not prior:
                return head
            prior = prior.next
            i += 1
    
        if not prior:
            head = head.next
            return head
        
        prev_deleted = head
        while prior.next:
            prior = prior.next
            prev_deleted = prev_deleted.next

        if prev_deleted and prev_deleted.next:
            prev_deleted.next = prev_deleted.next.next

        return head

            