class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # since no greater for the max element lets start from the max
        starting_index = nums.index(max(nums))
        i = 0
        n = len(nums)
        stack = []
        ans = [-1] * n
        for _ in range(n):
            j = i + starting_index
            while stack and nums[j] >= stack[-1]:
                stack.pop()
            if stack:
                ans[j] = stack[-1]
            stack.append(nums[j])
            i -= 1

        return ans

        