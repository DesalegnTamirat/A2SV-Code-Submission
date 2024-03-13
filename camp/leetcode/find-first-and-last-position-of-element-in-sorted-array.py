class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first(nums, target):
            left = 0
            right = len(nums) - 1
            answer = -1
            while left <= right:
                middle = (left + right) // 2
                if nums[middle] == target:
                    answer = middle
                
                if nums[middle] >= target:
                    right = middle - 1
                else:
                    left = middle + 1

            return answer
        
        def find_last(nums, target):
            answer = -1
            left = 0
            right = len(nums) - 1
            while left <= right:
                middle = (left + right) // 2
                if nums[middle] == target:
                    answer = middle
                
                if nums[middle] <= target:
                    left = middle + 1
                else:
                    right = middle - 1
            
            return answer
        
        return [find_first(nums, target), find_last(nums, target)]