class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        current_window = set(s[left])
        right = 1
        maximum = 1
        while right < len(s):
            while s[right] in current_window:
                current_window.remove(s[left])
                left += 1
            current_window.add(s[right])
            maximum = max(maximum, right - left + 1)
            right += 1

        return maximum