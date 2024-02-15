class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        prefix_sum = [nums[0]]
        minimum = 0 if nums[0] > 0 else nums[0]
        maximum = nums[0]
        for num in nums[1:]:
            prefix_sum.append(prefix_sum[-1] + num)
            maximum = max(prefix_sum[-1] - minimum, maximum)
            minimum = min(prefix_sum[-1], minimum)

        return maximum
            