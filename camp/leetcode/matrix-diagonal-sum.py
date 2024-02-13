class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if row == col or (row + col == len(mat) - 1):
                    ans += mat[row][col]
        
        return ans