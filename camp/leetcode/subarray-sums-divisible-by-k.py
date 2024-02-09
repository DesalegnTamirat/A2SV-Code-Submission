class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        remainder_count = {0: 1}
        accumulator = 0
        ans = 0
        for num in nums:
            accumulator += num
            remainder = accumulator % k
            if remainder in remainder_count:
                ans += remainder_count[remainder]
            
            remainder_count[remainder] = remainder_count.get(remainder, 0) + 1

        return ans
        
        