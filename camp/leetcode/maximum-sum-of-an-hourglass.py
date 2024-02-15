class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        maximum_sum = float("-inf")
        for row in range(len(grid) - 2):
            for col in range(len(grid[0]) - 2):
                r1 = grid[row][col] + grid[row][col + 1] + grid[row][col+2]
                r2 = grid[row + 1][col + 1]
                r3 = grid[row + 2][col] + grid[row + 2][col + 1] + grid[row + 2][col+2]
                maximum_sum = max(maximum_sum, r1 + r2 + r3)

        return maximum_sum