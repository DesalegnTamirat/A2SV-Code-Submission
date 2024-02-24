class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freq = Counter(t)
        needed = len(t_freq)
        left = 0
        minimum = float("inf")
        window = {}
        size = 0
        ans = [0, 0]
        for right in range(len(s)):
            if s[right] in t_freq:
                window[s[right]] = window.get(s[right], 0) + 1
                if window[s[right]] == t_freq[s[right]]:
                    size += 1
            
            while size == needed:
                if (right - left + 1) < minimum:
                    minimum = right - left + 1
                    ans = [left, right + 1]
                if s[left] in window:
                    window[s[left]] -= 1
                    if window[s[left]] < t_freq[s[left]]:
                        size -= 1
                left += 1

        return "".join(s[ans[0]: ans[1]])