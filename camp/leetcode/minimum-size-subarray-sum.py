class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minimum = float("inf")
        n = len(nums)
        left = right = total = 0
        while right < n:
            total += nums[right]
            if total >= target:
                minimum = min(minimum, right - left + 1)
            
            while total - nums[left] >= target:
                total -= nums[left]
                left += 1
                minimum = min(minimum, right - left + 1)
            
            right += 1

        if total >= target:
            minimum = min(minimum, right - left)
            
        return 0 if minimum == float("inf") else minimum