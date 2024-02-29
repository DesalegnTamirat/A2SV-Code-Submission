# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isvalid(root, left_bound, right_bound):
            if not root:
                return True
            if root.val >= right_bound or root.val <= left_bound:
                return False
            left_is_valid = isvalid(root.left, left_bound, root.val)
            right_is_valid = isvalid(root.right, root.val, right_bound)

            return left_is_valid and right_is_valid

        return isvalid(root, float("-inf"), float("inf"))
