class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        for letter in strs[0]:
            prefix = ans + letter
            for other in strs[1:]:
                if not other.startswith(prefix):
                    return ans
            ans = prefix
        return ans