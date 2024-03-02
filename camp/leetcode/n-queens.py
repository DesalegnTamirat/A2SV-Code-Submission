class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        major_diagonal = set()
        minor_diagonal = set()
        board = [["."]* n for _ in range(n)]
        result = []
        def backtrack(row):
            if row == n:
                result.append(["".join(cell) for cell in board])
                return
            
            for col in range(n):
                if col in cols:
                    continue
                if (row + col) in major_diagonal:
                    continue
                if (row - col) in minor_diagonal:
                    continue
                
                cols.add(col)
                major_diagonal.add(row + col)
                minor_diagonal.add(row - col)
                board[row][col] = "Q"

                backtrack(row + 1)

                cols.remove(col)
                major_diagonal.remove(row + col)
                minor_diagonal.remove(row - col)
                board[row][col] = "."

        backtrack(0)
        return result

                