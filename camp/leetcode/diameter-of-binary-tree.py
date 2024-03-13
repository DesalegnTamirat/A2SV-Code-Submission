# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maximum = 0
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def find_height(root):
            if not root:
                return 0
            
            left_height = find_height(root.left)
            right_height = find_height(root.right)
            self.maximum = max(self.maximum, left_height + right_height)
            return 1 + max(left_height, right_height)

        find_height(root)

        return self.maximum