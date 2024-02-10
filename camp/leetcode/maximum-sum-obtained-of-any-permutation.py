class Solution(object):
    def maxSumRangeQuery(self, nums, requests):
        """
        :type nums: List[int]
        :type requests: List[List[int]]
        :rtype: int
        """
        range_sum = [0 for _ in range(len(nums))]
        for start, end in requests:
            range_sum[start] += 1
            if end < len(nums) - 1:
                range_sum[end + 1] -= 1

        prefix_sum = []
        for num in range_sum:
            if prefix_sum:
                prefix_sum.append(prefix_sum[-1] + num)
            else:
                prefix_sum.append(num)
        
        prefix_sum.sort(reverse = True)
        nums.sort(reverse = True)
        total = 0
        for i in range(len(prefix_sum)):
            total += nums[i] * prefix_sum[i]

        return total % (10 ** 9 + 7)

