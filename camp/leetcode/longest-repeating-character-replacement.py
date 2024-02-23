class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maximum = 0
        counter = 0
        letter_freq = {}
        for right in range(len(s)):
            letter_freq[s[right]] = letter_freq.get(s[right], 0) + 1
            counter = max(counter, letter_freq[s[right]])
            while right - left + 1 - counter > k:
                letter_freq[s[left]] -= 1
                left += 1
            maximum = max(maximum, right - left + 1)

        return maximum