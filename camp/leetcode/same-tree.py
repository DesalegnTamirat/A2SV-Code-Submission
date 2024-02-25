# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p and not q) or (q and not p) or (q and p and q.val != p.val):
            return False
        if not p and not q:
            return True
        left_flag = self.isSameTree(p.left, q.left)
        right_flag = self.isSameTree(p.right, q.right)
        return left_flag and right_flag