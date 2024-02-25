# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def values(root):
            if not root:
                return []
            return values(root.left) + [root.val] + values(root.right)
        nums = values(root)
        nums.sort()
        return nums[k - 1]