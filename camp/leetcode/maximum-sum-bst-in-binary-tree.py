# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.maximum = 0
        def validate_sum(root):
            if not root:
                return float("inf"), float("-inf"), 0
            
            left_min, left_max, left_sum = validate_sum(root.left)
            right_min, right_max, right_sum = validate_sum(root.right)
            if left_min == None or right_min == None:
                return None, None, None
                
            if left_max < root.val < right_min:
                self.maximum = max(self.maximum, left_sum + right_sum + root.val)
                return min(left_min, root.val), max(right_max, root.val) ,left_sum + right_sum + root.val

            return None, None, None

        validate_sum(root)
        print(False == 0, None == 0)
        return max(self.maximum, 0)
        