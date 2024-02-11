# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = head
        cur_node = head
        while cur_node:
            while cur_node and cur_node.val == prev_node.val:
                cur_node = cur_node.next
            prev_node.next = cur_node
            prev_node = cur_node
        
        return head
        