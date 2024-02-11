# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # making the next node to be deleted instead of the given
        # we do that by just taking the next value to given
        deleted_node = node.next
        node.val = deleted_node.val
        node.next = deleted_node.next

        