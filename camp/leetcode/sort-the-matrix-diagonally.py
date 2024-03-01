class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        diagonal_nums = defaultdict(list)
        rows, cols = len(mat), len(mat[0])
        for row in range(rows):
            for col in range(cols):
                diagonal_nums[row - col].append(mat[row][col])
        
        for diagonal in diagonal_nums:
            diagonal_nums[diagonal] = sorted(diagonal_nums[diagonal], reverse = True)
        
        for row in range(rows):
            for col in range(cols):
                mat[row][col] = diagonal_nums[row - col].pop()

        return mat