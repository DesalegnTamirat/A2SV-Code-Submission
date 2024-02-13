# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node1 = headA
        node2 = headB
        jumped = False
        while True:
            if node1 == node2:
                return node1
            if node1.next:
                node1 = node1.next
            else:
                node1 = headB
                if not jumped:
                    jumped = True
                else:
                    return 
            if node2.next:
                node2 = node2. next
            else:
                node2 = headA
            
            
            
        

        