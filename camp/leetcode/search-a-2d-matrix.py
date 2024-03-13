class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                nums.append(matrix[row][col])
        
        n = len(nums)

        def search(nums, target, left, right):
            if left > right:
                return False
            
            middle = (left + right) // 2
            if nums[middle] == target:
                return True
            elif target > nums[middle]:
                return search(nums, target, middle + 1, right)
            else:
                return search(nums, target, left, middle - 1)

        return search(nums, target, 0, n - 1)
            