class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1:
            return []
        
        ans = []
        next_greater = []
        for i in range(len(nums2)):
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    next_greater.append(nums2[j])
                    break
            else:
                next_greater.append(-1)
        
        for i in range(len(nums1)):
            ans.append(next_greater[nums2.index(nums1[i])])

        return ans