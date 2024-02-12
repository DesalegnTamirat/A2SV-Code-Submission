# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        values = []
        node = head
        while node:
            values.append(node.val)
            node = node.next
        
        start = left - 1
        end = right - 1
        while start < end:
            values[start], values[end] = values[end], values[start]
            start += 1
            end -= 1
        
        node = head
        i = 0
        while node:
            node.val = values[i]
            node = node.next
            i += 1
        
        return head