class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n = len(nums2)
        next_greater = [-1] * n
        stack = []
        num_index = {}
        for i in range(n - 1, -1, -1):
            num = nums2[i]
            num_index[num] = i
            while stack and num > stack[-1]:
                stack.pop()
            if stack:
                next_greater[i] = stack[-1]
            stack.append(num)
        
        ans = []
        for num in nums1:
            ans.append(next_greater[num_index[num]])

        return ans
            