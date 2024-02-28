# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.value_count = {}
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # counting how many times each value occur
        self.pre_order_traverse(root)

        # taking the highest count
        highest_count = 0
        for count in self.value_count.values():
            highest_count = max(highest_count, count)
        
        # collecting all with the highest node
        modes = []
        for value, count in self.value_count.items():
            if count == highest_count:
                modes.append(value)
        
        return modes

    def pre_order_traverse(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return 
        
        value = root.val
        self.value_count[value] = self.value_count.get(value, 0) + 1
        self.pre_order_traverse(root.left)
        self.pre_order_traverse(root.right)


