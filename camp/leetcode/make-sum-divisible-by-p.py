class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        if sum(nums) % p == 0:
            return 0

        target = sum(nums) % p
        remainder_index = {0:-1} #we can't remove the whole array so 0 -> -1
        n = len(nums)
        remainder = 0
        ans = n
        accumulator = 0
        for i,num in enumerate(nums):
            accumulator += num
            remainder = accumulator % p
            # checking if other subarray in hashtable that complements
            if (remainder - target) % p in remainder_index:
                ans = min(ans, i - remainder_index.get((remainder - target) % p))
            remainder_index[remainder] = i
        
        return -1 if ans == n else ans