# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        result = []
        def bfs(root):
            if not root:
                return []
            queue = deque()
            queue.append(root)
            while queue:
                values = []
                level = len(result) + 1
                for i in range(len(queue)):
                    front = queue.popleft()
                    values.append(front.val)
                    if front.left:
                        queue.append(front.left)
                    if front.right:
                        queue.append(front.right)
                result.append(values)
            return result
        
        def check(nums_list):
            for i, nums in enumerate(nums_list):
                for j, num in enumerate(nums):
                    if i % 2 == 0 and (num % 2 == 0 or (j > 0 and num <= nums[j - 1])):
                        return False
                    if i % 2 == 1 and (num % 2 == 1 or (j > 0 and num >= nums[j - 1])):
                        return False
            
            return True
        bfs(root)
        print(result)
        return check(result)
