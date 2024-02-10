class Solution:
    def maxScore(self, s: str) -> int:
        maximum = 0
        right = s.count("1")
        left = 0
        for let in s[:-1]:
            if let == "0":
                left += 1
            else:
                right -= 1
            maximum = max(maximum, right + left)

        return maximum