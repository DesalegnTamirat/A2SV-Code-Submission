class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        maximum = 1
        once_zero_used = False
        while right < len(nums):
            zero_used = False
            while right < len(nums) and (nums[right] == 1 or not zero_used):
                if nums[right] == 0:
                    next_index = right + 1
                    zero_used = True
                    once_zero_used = True
                right += 1
            maximum = max(maximum, right - left)
            left = next_index if zero_used else 0
        
        return maximum - 1