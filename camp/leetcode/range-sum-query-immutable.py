class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.prefix_sum = self.find_prefix_sum()

    def find_prefix_sum(self):
        prefix_sum = [0]
        for num in self.nums:
            prefix_sum.append(prefix_sum[-1] + num)
        
        return prefix_sum
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.prefix_sum[right + 1] - self.prefix_sum[left]

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)