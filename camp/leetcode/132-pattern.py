class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = []
        minimum = float("inf")
        for num in nums:
            while stack and num >= stack[-1][0]:
                stack.pop()
            
            if stack and num > stack[-1][1]:
                return True
            minimum = min(minimum, num)
            stack.append((num, minimum))
        
        return False
            