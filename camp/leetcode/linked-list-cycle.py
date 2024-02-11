# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # checking if we have encountered this node before
        encountered = set()
        node = head
        while node:
            if node in encountered:
                return True
            encountered.add(node)
            node = node.next

        return False