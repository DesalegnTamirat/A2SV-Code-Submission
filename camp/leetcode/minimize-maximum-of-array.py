class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        maximum = nums[0]
        total = nums[0]
        i = 1
        while i < len(nums):
            total += nums[i]
            average = ceil(total / (i + 1))
            maximum = max(maximum, average)
            i += 1

        return maximum
        