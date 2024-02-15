class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start = 0
        end = k - 1
        total = sum(nums[:end + 1])
        maximum = total
        while start < len(nums) - k:
            start += 1
            end += 1
            total += nums[end] - nums[start - 1]
            maximum = max(maximum, total)

        return maximum / k