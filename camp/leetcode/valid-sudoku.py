class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_value = {i: set() for i in range(9)}
        col_value = {j: set() for j in range(9)}
        subboxes = {n: set() for n in range(9)}
        for row in range(9):
            for col in range(9):
                print(subboxes)
                value = board[row][col]
                if value == ".":
                    continue
                if value in row_value[row]:
                    return False
                elif value in col_value[col]:
                    return False
                elif value in subboxes[(row // 3) * 3 + col // 3]:
                    return False
                row_value[row].add(value)
                col_value[col].add(value)
                subboxes[(row // 3) * 3 + col // 3].add(value)
        
        return True