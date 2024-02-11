# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        less = greater = less_head = greater_head = None
        node = head
        while node:
            if node.val < x:
                if not less:
                    less = node
                    less_head = node
                else:
                    less.next = node
                    less = less.next
            else:
                if not greater:
                    greater = node
                    greater_head = node
                else:
                    greater.next = node
                    greater = greater.next
            node = node.next
        if not greater_head:
            return less_head
        if not less_head:
            return greater_head
        greater.next = None
        less.next = greater_head
        return less_head