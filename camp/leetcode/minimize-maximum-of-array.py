class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        maximum = nums[0]
        total = nums[0]
        i = 1
        while i < len(nums):
            total += nums[i]
            if nums[i] > maximum:
                value = ceil(total / (i + 1))
                maximum = max(maximum, value)
            print(maximum)
            i += 1

        return maximum
        