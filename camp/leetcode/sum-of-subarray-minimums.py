class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        results = arr[:]
        stack = []
        # to how many subarray are each minimum to the right
        for i in range(n - 1, -1, -1):
            while stack and arr[i] < stack[-1][0]:
                stack.pop()
            
            if stack:
                results[i] *= stack[-1][1] - i
            else:
                results[i] *= n - 1 - i + 1
            
            stack.append((arr[i], i))

        # to how many subarrays are they minimum to the left
        stack = []
        for j in range(n):
            while stack and arr[j] <= stack[-1][0]:
                stack.pop()
            
            if stack:
                results[j] *= j - stack[-1][1]
            else:
                results[j] *= j + 1
            
            stack.append((arr[j], j))
        
        return sum(results) % (10 ** 9 + 7)
        
        
        