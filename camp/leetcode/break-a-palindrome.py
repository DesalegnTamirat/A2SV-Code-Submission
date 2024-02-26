class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) < 2:
            return ""
        ans = list(palindrome)
        for i in range(len(ans)):
            if ans[i] != "a":
                if len(ans) % 2 == 1 and i == len(ans) // 2:
                    break
                ans[i] = "a"
                return "".join(ans)
        ans[-1] = "b"
        return "".join(ans)
            