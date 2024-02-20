class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        values = set()
        total = 0
        maximum = 0
        left = 0
        for num in nums:
            while num in values:
                total -= nums[left]
                values.remove(nums[left])
                left += 1
            
            total += num
            values.add(num)
            maximum = max(maximum, total)

        return maximum

        
        