class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total_sum = sum(nums)
        left_sum = 0
        ans = []
        n = len(nums)
        for i in range(n):
            right_sum = total_sum - nums[i] - left_sum
            sum_after_it = right_sum - nums[i] * (n - i - 1)
            sum_before_it = nums[i] * (i) - left_sum
            ans.append(sum_after_it + sum_before_it)
            left_sum += nums[i]
        
        return ans