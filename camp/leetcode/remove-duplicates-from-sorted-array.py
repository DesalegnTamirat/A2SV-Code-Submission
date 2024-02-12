class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        prev = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[prev]:
                nums[i] = False
                length -= 1
            else:

                prev = i
        
        print(nums)
        write = read = 0
        while read < len(nums):
            if nums[read] is not False:
                nums[read], nums[write] = nums[write], nums[read]
                write += 1
            read += 1

        return length
