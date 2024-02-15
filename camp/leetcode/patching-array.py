class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        i = 0
        num = 1
        upto = 0
        patches = 0
        while num <= n:
            if i >= len(nums) or nums[i] > num:
                patches += 1
                upto += num
                num = upto + 1 
            while i < len(nums) and num >= nums[i]:
                upto += nums[i]
                i += 1
                num = upto + 1
        
        return patches
            
            
            