class Solution(object):
    def subsets(self, nums):
        ans = []
        subset = []
        def backtrack(index):
            if index == len(nums):
                ans.append(subset.copy())
                return 
            
            # including value on index i
            subset.append(nums[index])
            backtrack(index + 1)
            # not including it
            subset.remove(nums[index])
            backtrack(index + 1)
        
        # starting index would be zero
        backtrack(0)
        return ans
        