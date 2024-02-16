class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        count = 0
        n = len(nums)
        for i in range(n - 2):
            start = i + 1
            end = n - 1
            while start < end:
                if nums[i] < nums[start] + nums[end]:
                    count += end - start
                    start += 1
                else:
                    end -= 1
        
        return count
