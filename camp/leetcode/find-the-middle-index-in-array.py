class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        
        total_sum = prefix_sum[-1]
        for i in range(1, len(nums) + 1):
            if prefix_sum[i - 1] == total_sum - prefix_sum[i]:
                return i - 1

        return -1