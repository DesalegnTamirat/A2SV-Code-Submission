# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height_balanced(root):
            if not root:
                return 0, True

            left_height, l_balanced =height_balanced(root.left)
            right_height, r_balanced =height_balanced(root.right)

            return 1 + max(left_height, right_height), l_balanced and r_balanced and abs(right_height - left_height) <= 1
        
        return height_balanced(root)[1]