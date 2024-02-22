class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        odds = 0
        nices = 0
        prev_left = 0
        n = len(nums)
        for right in range(n):
            if nums[right] % 2 == 1:
                odds += 1
            
            while odds - (nums[left] % 2 == 1) >= k:
                if nums[left] % 2 == 1:
                    odds -= 1
                    prev_left = left + 1
                left += 1
            
            if odds == k:
                nices += left + 1 - prev_left
        
        return nices 