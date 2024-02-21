# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2, head = None, tail = None):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1 and not list2:
            return head
        elif not list2 or list1 and list1.val < list2.val:
            temp = list1.next
            list1.next = None
            if head:
                tail.next = list1
                tail = list1
            else:
                head = list1
                tail = list1
            return self.mergeTwoLists(temp, list2, head, tail)
        else:
            temp = list2.next
            list2.next = None
            if head:
                tail.next = list2
                tail = list2
            else:
                head = list2
                tail = list2
            return self.mergeTwoLists(list1, temp, head, tail)
        
        
        