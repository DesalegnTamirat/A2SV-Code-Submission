class Solution(object):
    
    def myPow(self, x, n):
        def pos_pow(x, n):
            if n == 0:
                return 1
            ans = self.myPow(x, n // 2)
            ans *= ans
            if n % 2 == 1:
                ans *= x
            return ans
        
        if n < 0:
            return 1 / pos_pow(x, abs(n))
        return pos_pow(x, n)