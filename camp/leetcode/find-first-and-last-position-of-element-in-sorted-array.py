class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.starting(nums, target), self.ending(nums, target)]

    def starting(self, nums, target):
        start, end = 0, len(nums) - 1
        first = -1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                first = mid
                end = mid - 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return first

    def ending(self, nums, target):
        last = -1
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                last = mid
                start = mid + 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        
        return last