# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return
        
        n = len(nums)
        middle = (n - 1) // 2
        root = ListNode(nums[middle])
        root.right = self.sortedArrayToBST(nums[middle + 1 : ])
        root.left = self.sortedArrayToBST(nums[ : middle])

        return root