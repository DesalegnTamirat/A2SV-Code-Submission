class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        value_indices = defaultdict(list)
        for i, num in enumerate(nums):
            value_indices[num].append(i)
        
        ans = [0] * len(nums)
        for num in value_indices:
            [0, 2, 3, 4]
            indices = value_indices[num]
            if len(indices) > 1:
                right = sum(indices)
                left = 0
                for i, index in enumerate(indices):
                    right -= index
                    ans[index] += right - index * (len(indices) - i - 1)
                    ans[index] += index * i - left
                    left += index
        
        return ans

