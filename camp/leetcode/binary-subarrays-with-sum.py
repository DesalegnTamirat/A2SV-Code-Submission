class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        prefix_sum_counter = {0: 1}
        accumulator = 0
        ans = 0
        for num in nums:
            accumulator += num
            if (accumulator - goal) in prefix_sum_counter:
                ans += prefix_sum_counter[accumulator - goal]
            
            prefix_sum_counter[accumulator] = prefix_sum_counter.get(accumulator, 0) + 1

        return ans