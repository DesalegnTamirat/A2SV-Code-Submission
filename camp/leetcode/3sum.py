class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        num_index = {num: index for index, num in enumerate(nums)}
        triplets = set()
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if j <= i:
                    continue
                num3 = 0 - num1 - num2
                if num3 in num_index:
                    k = num_index[num3]
                    if k <= j:
                        continue
                    triplets.add(tuple(sorted((nums[i], nums[j], nums[k]))))

        return [list(triplet) for triplet in triplets]

        
                
        