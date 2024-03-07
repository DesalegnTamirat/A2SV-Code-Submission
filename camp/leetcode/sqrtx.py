class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            middle = (left + right) // 2
            square = middle ** 2
            if square == x:
                return middle
            elif square > x:
                right = middle - 1
            else:
                answer = middle
                left = middle + 1
        
        return answer