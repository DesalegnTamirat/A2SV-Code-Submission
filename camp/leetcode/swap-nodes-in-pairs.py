# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        head.next.next = self.swapPairs(head.next.next)
        temp_node = head.next.next
        head.next.next = None
        # reversing the two nodes
        temp = head.next
        head.next = None
        temp.next = head
        head = temp
        head.next.next = temp_node
        return head
