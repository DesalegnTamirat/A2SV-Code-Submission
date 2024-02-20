class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        ans = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            temp = temperatures[i]
            # assuring if the stack monotonically increases
            while stack and temp >= stack[-1][0]:
                stack.pop()
            
            # if empty stack no greater temperature
            # else the top is the greater
            if not stack:
                ans[i] = 0
            else:
                ans[i] = stack[-1][1] - i
            
            stack.append((temp, i))
        
        return ans


        