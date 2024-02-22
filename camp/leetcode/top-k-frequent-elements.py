class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        nums = list(set(nums))
        return sorted(nums, key=lambda num: frequency[num], reverse=True)[:k]