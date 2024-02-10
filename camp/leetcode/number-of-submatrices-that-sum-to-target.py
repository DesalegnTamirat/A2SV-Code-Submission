class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        rows, cols = len(matrix), len(matrix[0])
        prefix_sum = []
        # calculating prefix sum for every rows 
        for row in range(rows):
            array = [matrix[row][0]]
            for col in range(1, cols):
                array.append(array[-1] + matrix[row][col])
            prefix_sum.append(array)

        # taking a specific column as end point
        # and counting how much submatrix sum to target
        count = 0
        for c1 in range(cols):
            for c2 in range(c1, cols):
                prefix_sum_count = {0: 1}
                sum_val = 0

                for row in range(rows):
                    sum_val += prefix_sum[row][c2] - (prefix_sum[row][c1 - 1] if c1 > 0 else 0)
                    count += prefix_sum_count.get(sum_val - target, 0)
                    prefix_sum_count[sum_val] = prefix_sum_count.get(sum_val, 0) + 1

        return count
