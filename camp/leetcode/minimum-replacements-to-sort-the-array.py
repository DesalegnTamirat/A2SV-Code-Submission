class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        prev = nums[-1]
        n = len(nums)
        count = 0
        for i in range(n - 2, -1, -1):
            if nums[i] > prev:
                diff = nums[i] - prev
                part = ceil(diff / prev + 1)
                prev = ceil(nums[i] // part)
                count += part - 1
            else:
                prev = nums[i]

        return count
       