class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        maximum = 0
        n = len(nums)
        while right < n and left < n:
            while right < n and (k > 0 or nums[right] == 1):
                if nums[right] == 0:
                    k -= 1
                right += 1
            
            maximum = max(maximum, right - left)
            if nums[left] == 0:
                k += 1
            left += 1
            
        return max(maximum, right - left)
            