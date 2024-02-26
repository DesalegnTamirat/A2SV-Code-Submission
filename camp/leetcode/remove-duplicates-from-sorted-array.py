class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        for right in range(len(nums)):
            if nums[left] != nums[right]:
                left += 1
                nums[left], nums[right] = nums[right], nums[left]
        
        return left + 1
