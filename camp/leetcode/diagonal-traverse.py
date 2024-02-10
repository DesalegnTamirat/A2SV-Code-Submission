class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # store elements of the same diagonal
        row_col_diagonal = {}
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                key = row + col
                if key in row_col_diagonal:
                    row_col_diagonal[key].append(mat[row][col])
                else:
                    row_col_diagonal[key] = [mat[row][col]]
        
        print(row_col_diagonal)
        ans = []
        for key in row_col_diagonal:
            if key % 2 == 0:
                ans.extend(reversed(row_col_diagonal[key]))
            else:
                ans.extend(row_col_diagonal[key])
        
        return ans
        
