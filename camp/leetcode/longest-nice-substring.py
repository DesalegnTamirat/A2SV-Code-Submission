class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def check(s):
            counter = Counter(s)
            for letter in counter:
                if letter.isupper() and letter.lower() not in counter:
                    return False
                elif letter.islower() and letter.upper() not in counter:
                    return False

            return True

        n = len(s)
        ans = ""
        minimum = float("-inf")
        for i in range(n):
            for j in range(i + 1, n):
                sub = s[i: j + 1]
                if check(sub) and len(sub) > minimum:
                    minimum = len(sub)
                    ans = sub

        return ans


    