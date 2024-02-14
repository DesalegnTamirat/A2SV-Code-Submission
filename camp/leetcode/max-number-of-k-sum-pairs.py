class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        start = operations = 0
        end = len(nums) - 1
        while start < end:
            sums = nums[start] + nums[end]
            if sums == k:
                operations += 1
                start += 1
                end -= 1
            elif sums > k:
                end -= 1
            else:
                start += 1
        
        return operations
        