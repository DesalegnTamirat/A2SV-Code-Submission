class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []
        nums.sort()
        def backtrack(i):
            if i == len(nums):
                ans.append(subset.copy())
                return
            
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()
            
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1) 

        backtrack(0)
        return ans