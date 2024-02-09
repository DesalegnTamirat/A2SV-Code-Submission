class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for row in range(1, len(matrix)): 
            for col in range(1, len(matrix[0])):
                if matrix[row][col] != matrix[row - 1][col - 1]:
                    # checking weather this element equal with prior elem
                    return False
        
        return True
