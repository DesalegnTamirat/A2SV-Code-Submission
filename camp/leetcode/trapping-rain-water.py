class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        postfix_maximum = [0] * n
        maximum = height[-1]
        for i in range(n - 2, -1, -1):
            postfix_maximum[i] = maximum
            maximum = max(maximum, height[i])
        
        prefix_maximum = [0] * n
        maximum = height[0]
        for i in range(1, n):
            prefix_maximum[i] = maximum
            maximum = max(maximum, height[i])

        answer = 0
        for i in range(n):
            next_maximum = postfix_maximum[i]
            prev_maximum = prefix_maximum[i]
            current = height[i]
            if current < next_maximum and current < prev_maximum:
                answer += min(next_maximum, prev_maximum) - current

        return answer
                
