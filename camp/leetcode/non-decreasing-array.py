class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modified = False
        prev = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            if num < prev:
                if modified:
                    return False
                else:
                    if i < len(nums) - 1 and prev > nums[i + 1]:
                        if i > 1 and nums[i] < nums[i - 2]:
                            return False
                        prev = num
                    modified = True
            else:
                prev = num
        
        return True