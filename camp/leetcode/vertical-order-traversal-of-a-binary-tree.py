# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        pos_val = defaultdict(list)

        def pre_order(root, row, col):
            if not root:
                return
            pos_val[(row, col)].append(root.val)
            pre_order(root.left, row + 1, col - 1)
            pre_order(root.right, row + 1, col + 1)

        pre_order(root, 0, 0)
        result = []
        prev_col = float("inf")
        for pos in sorted(pos_val, key = lambda pos: (pos[1], pos[0])):
            row, col = pos
            if col != prev_col:
                result.append([])
                prev_col = col
            result[-1].extend(sorted(pos_val[pos]))

        return result
