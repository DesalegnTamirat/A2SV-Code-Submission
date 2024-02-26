class Solution:
    def numberOfWays(self, s: str) -> int:
        total_zero = s.count("0")
        total_one = s.count("1")
        zeros = 0
        ones = 0
        ans = 0
        for bit in s:
            if bit == "0":
                ans += ones * (total_one - ones)
                zeros += 1
            else:
                ans += zeros * (total_zero - zeros)
                ones += 1

        return ans
        