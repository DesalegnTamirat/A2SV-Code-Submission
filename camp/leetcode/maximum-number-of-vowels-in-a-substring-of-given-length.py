class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        max_vowels = 0
        i = 0
        vowels = {"a", "e", "i", "o", "u"}
        while i < k and i < n:
            if s[i] in vowels:
                max_vowels += 1
            i += 1
        
        left = 1
        right = k
        vowels_count = max_vowels
        while right < n:
            if s[right] in vowels:
                vowels_count += 1
            if s[left - 1] in vowels:
                vowels_count -= 1
            max_vowels = max(max_vowels, vowels_count)
            left += 1
            right += 1
        
        return max_vowels


