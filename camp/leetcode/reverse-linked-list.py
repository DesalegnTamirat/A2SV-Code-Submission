# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # storing somewhere and linking them in reverse order
        nodes = []
        node = head
        while node:
            temp = node.next
            node.next = None
            nodes.append(node)
            node = temp

        head = nodes[-1]
        node = head
        for i in range(len(nodes) - 2, -1, -1):
            node.next = nodes[i]
            node = nodes[i]
        
        return head