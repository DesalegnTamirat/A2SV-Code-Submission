class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pairs = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if i * j % k == 0 and nums[i] == nums[j]:
                    pairs += 1
        return pairs


        