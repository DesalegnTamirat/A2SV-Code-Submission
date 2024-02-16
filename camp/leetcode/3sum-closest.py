class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort(reverse = True)
        min_abs_diff = float("inf")
        n = len(nums)
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            while left < right:
                triple_sum = nums[i] + nums[left] + nums[right]
                abs_diff = abs(target - triple_sum)
                if abs_diff < min_abs_diff:
                    ans = triple_sum
                    min_abs_diff = abs_diff
                if triple_sum == target:
                    return triple_sum
                elif triple_sum < target:
                    right -= 1
                else:
                    left += 1
        
        return ans