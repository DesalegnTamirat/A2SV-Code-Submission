class Solution(object):
    def fib(self, n):
        return n if n in {0, 1} else self.fib(n - 1) + self.fib(n - 2) 
        