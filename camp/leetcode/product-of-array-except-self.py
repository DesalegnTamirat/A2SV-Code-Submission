class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = [1]
        suffix = [1]

        for num in nums:
            prefix.append(prefix[-1] * num)

        for num in nums[::-1]:
            suffix.append(suffix[-1] * num)
        
        suffix.reverse()

        ans = []
        for i in range(1, len(nums) + 1):
            ans.append(prefix[i - 1] * suffix[i])

        return ans
            
        