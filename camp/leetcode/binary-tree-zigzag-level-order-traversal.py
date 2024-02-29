# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        result = []
        while queue:
            values = []
            for i in range(len(queue)):
                front = queue.popleft()
                values.append(front.val)
                if front.left:
                    queue.append(front.left)
                if front.right:
                    queue.append(front.right)
            
            result.append(values)
            
        for i, values in enumerate(result):
            if i % 2 == 1:
                result[i] = reversed(values)

        return result

        