class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = {row: set() for row in range(9)}
        cols = {col: set() for col in range(9)}
        cells = {cell: set() for cell in range(9)}
        unfilled = []
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] != ".":
                    value = board[row][col]
                    rows[row].add(value)
                    cols[col].add(value)
                    cells[(row // 3) * 3 + col // 3].add(value)
                else:
                    unfilled.append([row, col])
        
        options = "123456789"
        def backtrack():
            if not unfilled:
                return True
            row, col = unfilled[-1]
            for num in options:
                if num in rows[row] or num in cols[col]:
                    continue
                if num in cells[(row // 3) * 3 + col // 3]:
                    continue

                board[row][col] = num
                rows[row].add(num)
                cols[col].add(num)
                cells[(row // 3) * 3 + col // 3].add(num)
                unfilled.pop()
                if backtrack():
                    return True

                board[row][col] = "."
                rows[row].remove(num)
                cols[col].remove(num)
                cells[(row // 3) * 3 + col // 3].remove(num)
                unfilled.append([row, col])
            return False

        backtrack()
            

    