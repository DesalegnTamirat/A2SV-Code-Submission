# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(None)
        dummy_node.next = head
        prev_node = head
        current_node = prev_node.next

        while current_node:
            if current_node.val > prev_node.val:
                prev_node = current_node
                current_node = current_node.next
                continue
            
            node = dummy_node
            while current_node.val > node.next.val:
                node = node.next

            prev_node.next = current_node.next
            current_node.next = node.next
            node.next = current_node
            
            current_node = prev_node.next

        return dummy_node.next