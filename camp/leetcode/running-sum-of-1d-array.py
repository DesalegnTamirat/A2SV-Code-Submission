class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        accumulator = 0
        running_sum = []
        for num in nums:
            accumulator += num
            running_sum.append(accumulator)

        return running_sum