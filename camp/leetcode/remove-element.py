class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        start = 0
        end = n - 1
        while start < end:
            if nums[start] == val:
                if nums[end] != val:
                    nums[start], nums[end] = nums[end], nums[start]
                    start += 1
                    end -= 1
                else:
                    end -= 1
            else:
                start += 1
        
        length = 0
        for num in nums:
            if num != val:
                length += 1
            else:
                return length