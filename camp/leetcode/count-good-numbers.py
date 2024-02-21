class Solution(object):
    def pow_mod(self, num, base, mod):
        if num == 0:
            return 1
        answer = self.pow_mod(num//2, base, mod)
        if num % 2 == 0:
            mult = 1
        else:
            mult = base
        answer *= answer * mult
        return answer % mod
        
    def countGoodNumbers(self, n):
        m = 10**9 + 7
        odds = n // 2
        evens = n - odds
        return self.pow_mod(evens, 5, m) * self.pow_mod(odds, 4, m) % m
        