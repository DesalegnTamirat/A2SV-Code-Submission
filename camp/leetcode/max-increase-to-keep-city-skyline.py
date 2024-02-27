class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        # finding the maximum of each row and col
        row_maximum = {}
        col_maximum = {}
        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                value = grid[row][col]
                if row not in row_maximum or value > row_maximum[row]:
                    row_maximum[row] = value
                if col not in col_maximum or value > col_maximum[col]:
                    col_maximum[col] = value
        
        # for every value increasing it to maximum
        # but can't exceed both row and col maximum of its location
        answer = 0
        for row in range(rows):
            for col in range(cols):
                value = grid[row][col]
                if value < row_maximum[row] and value < col_maximum[col]:
                    answer += min(row_maximum[row], col_maximum[col]) - value
        
        return answer