class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_frequency = {}
        nums2_frequency = {}
        for num1 in nums1:
            nums1_frequency[num1] = nums1_frequency.get(num1, 0) + 1
        
        for num2 in nums2:
            nums2_frequency[num2] = nums2_frequency.get(num2, 0) + 1
        
        ans = []
        for num1 in nums1_frequency:
            if num1 in nums2_frequency:
                ans.extend([num1] * min(nums1_frequency[num1], nums2_frequency[num1]))

        return ans        