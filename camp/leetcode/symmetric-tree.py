# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def same(root1, root2):
            if not root1 and root2 or not root2 and root1:
                return False
            elif not root1 and not root2:
                return True
            elif root1.val != root2.val:
                return False
            
            return same(root1.left, root2.right) and same(root1.right, root2.left)

        return same(root.left, root.right)
            

    