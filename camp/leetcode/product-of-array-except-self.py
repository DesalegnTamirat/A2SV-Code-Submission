class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1 for _ in range(n)]
        # forward product
        forward = 1
        for i in range(n - 1):
            forward *= nums[i]
            ans[i + 1] *= forward
        
        # backward product
        backward = 1
        for i in range(n - 1, 0, -1):
            backward *= nums[i]
            ans[i - 1] *= backward

        return ans
