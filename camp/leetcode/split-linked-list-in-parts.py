# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        if head is None:
            return [None] * k
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        size = length // k
        one_larger = length % k
        normals = k - one_larger
        parts = []
        prev_head = head
        while one_larger > 0:
            counter = size + 1
            node = prev_head
            while counter > 1:
                node = node.next
                counter -= 1
            
            temp = node.next
            node.next = None
            parts.append(prev_head)
            prev_head = temp
            one_larger -= 1


        while normals > 0:
            normals -= 1
            if prev_head is None:
                parts.append(prev_head)
                continue
            counter = size
            node = prev_head
            while counter > 1:
                node = node.next
                counter -= 1
            
            temp = node.next
            node.next = None
            parts.append(prev_head)
            prev_head = temp

        return parts


        