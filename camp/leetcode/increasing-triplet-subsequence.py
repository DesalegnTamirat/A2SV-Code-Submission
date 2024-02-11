class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        first_min = float("inf")
        second_min = float("inf")
        for i in range(n):
            if nums[i] <= first_min:
                first_min = nums[i]
            elif nums[i] > first_min and nums[i] <= second_min:
                second_min = nums[i]
            else:
                return True
            
        
        return False