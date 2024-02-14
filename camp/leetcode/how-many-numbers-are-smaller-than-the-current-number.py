class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_smaller = {}
        for index, num in enumerate(sorted(nums)):
            if num not in num_smaller: 
                num_smaller[num] = index
             
        return [num_smaller[num] for num in nums]

        