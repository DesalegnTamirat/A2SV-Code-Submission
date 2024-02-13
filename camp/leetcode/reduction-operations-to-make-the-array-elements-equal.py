class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        prev = nums[0]
        step = 0
        operations = 0
        for num in nums:
            if num != prev:
                prev = num
                step += 1
            operations += step
        
        return operations
