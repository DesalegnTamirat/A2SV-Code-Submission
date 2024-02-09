class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        n = len(matrix[0])
        answer = [[0 for i in range(m)] for j in range(n)]
        for i in range(m):
            for j in range(n):
                answer[j][i] = matrix[i][j]

        return answer
        