class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ans = [[0] * len(matrix) for _ in range(len(matrix[0]))]

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                ans[col][len(matrix) - row - 1] = matrix[row][col]
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                matrix[row][col] = ans[row][col]