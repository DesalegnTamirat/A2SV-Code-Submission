class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        total = 0
        nums.sort()
        i = 0
        for i in range(0, len(nums), 2):
            total += nums[i]

        return total
        