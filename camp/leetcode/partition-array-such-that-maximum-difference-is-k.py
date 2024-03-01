class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        answer = 1
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - prev > k:
                answer += 1
                prev = nums[i]
            
        return answer