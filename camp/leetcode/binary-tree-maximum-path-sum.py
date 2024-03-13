# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.maximum = float("-inf")
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def path_sum(root):
            if not root:
                return 0
            
            left_path = path_sum(root.left)
            right_path = path_sum(root.right)

            if left_path < 0:
                left_path = 0
            if right_path < 0:
                right_path =0
            
            self.maximum = max(self.maximum, left_path + root.val + right_path)
            
            return root.val + max(left_path, right_path)

        path_sum(root)

        return self.maximum