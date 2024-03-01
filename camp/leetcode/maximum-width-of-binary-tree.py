# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque()
        value = 1
        level = 0
        queue.append((root, value, level))
        prev_value = 1
        prev_level = 0
        answer = 0
        while queue:
            front, value, level = queue.popleft()
            if level > prev_level:
                prev_value = value
                prev_level = level
            
            answer = max(answer, value - prev_value + 1)
            if front.left:
                queue.append((front.left, 2 * value, level + 1))
            if front.right:
                queue.append((front.right, 2 * value + 1, level + 1))

        return answer

