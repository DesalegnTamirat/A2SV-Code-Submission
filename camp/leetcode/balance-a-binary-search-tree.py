# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sorted_roots = []

    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.pick(root)
        balanced_bst = self.sorted_to_bst(0, len(self.sorted_roots) - 1)
        return balanced_bst
        
    def pick(self, root):
        if not root:
            return
        self.pick(root.left)
        self.sorted_roots.append(root)
        self.pick(root.right)
    
    def sorted_to_bst(self, left, right):
        if left > right:
            return None
        
        middle = (left + right) // 2
        root = self.sorted_roots[middle]
        root.left = self.sorted_to_bst(left, middle - 1)
        root.right = self.sorted_to_bst(middle + 1, right)
        return root    

    
