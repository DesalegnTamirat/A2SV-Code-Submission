# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.number(root, 0)

    def number(self, root, total):
        if not root:
            return 0

        if not root.left and not root.right:
            return total * 10 + root.val
        
        left = self.number(root.left, total * 10 + root.val)
        right = self.number(root.right, total * 10 + root.val)
        return left + right
        
         