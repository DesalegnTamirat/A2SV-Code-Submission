class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        def backtrack(i):
            if len(path) == len(nums):
                ans.append(path.copy())
                return 
            sets = set(path)
            for i in range(len(nums)):
                if nums[i] not in sets:
                    path.append(nums[i])
                    backtrack(i + 1)
                    path.pop()
        
        backtrack(0)
        return ans