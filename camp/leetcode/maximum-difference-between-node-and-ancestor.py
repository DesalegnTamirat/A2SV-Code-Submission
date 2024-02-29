# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_des, min_des = self.max_min_descendant(root)
        difference = max(max_des - root.val, root.val - min_des)
        return max(difference, self.maxAncestorDiff(root.left), self.maxAncestorDiff(root.right))
    
    def max_min_descendant(self, root):
        if not root:
            return [float("-inf"), float("inf")]

        left_max, left_min = self.max_min_descendant(root.left)
        right_max, right_min = self.max_min_descendant(root.right)
        maximum = max(left_max, right_max, root.val)
        minimum = min(left_min, right_min, root.val)

        return [maximum, minimum]
       