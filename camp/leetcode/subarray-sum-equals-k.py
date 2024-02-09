class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        prefix_sum = 0
        sum_counter = {0: 1}
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in sum_counter:
                ans += sum_counter[prefix_sum - k]
            sum_counter[prefix_sum] = sum_counter.get(prefix_sum, 0) + 1
            
        return ans
        
        

        