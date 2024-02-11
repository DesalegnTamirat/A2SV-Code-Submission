# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        even = head
        odd = head.next
        odd_head = head.next
        if not head or not head.next:
            return head
        
        while even.next and odd.next:
            even.next = odd.next
            even = even.next
            odd.next = even.next 
            odd = odd.next
        
        even.next = odd_head
        return head
        