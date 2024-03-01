class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        paths = set()
        def backtrack(row, col, i):
            if (row, col) in paths:
                return False
            if row >= rows or row < 0 or col >= cols or col < 0:
                return False
            if board[row][col] != word[i]:
                return False
            if i == len(word) - 1:
                return True
            
            paths.add((row, col))
            left = backtrack(row, col + 1, i + 1)
            right = backtrack(row, col - 1, i + 1)
            up = backtrack(row - 1, col, i + 1)
            down = backtrack(row + 1, col, i + 1)
            paths.remove((row, col))
            return right or left or up or down

        for row in range(rows):
            for col in range(cols):
                word_found = backtrack(row, col, 0)    
                if  word_found:
                    return True
        return False
            