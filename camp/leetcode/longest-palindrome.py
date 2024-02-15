class Solution:
    def longestPalindrome(self, s: str) -> int:
        letter_frequency = Counter(s)
        length = 0
        can_add_one = 0
        for _, value in letter_frequency.items():
            if value % 2 == 0:
                length += value
            else:
                can_add_one = 1
                length += value - 1
        
        return length + can_add_one