class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        k = len(set(nums))
        elements = {}
        left = 0
        completes = 0
        for right in range(len(nums)):
            elements[nums[right]] = elements.get(nums[right], 0) + 1
            while len(elements) == k:
                if elements[nums[left]] > 1:
                    elements[nums[left]] -= 1
                    left += 1
                else:
                    break
            if len(elements) == k:
                completes += left + 1
        
        return completes