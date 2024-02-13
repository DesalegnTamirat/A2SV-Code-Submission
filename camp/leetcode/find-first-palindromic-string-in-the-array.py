class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            start = 0
            end = len(word) - 1
            while start < end:
                if word[start] != word[end]:
                    break
                start += 1
                end -= 1
            else:
                return word
        
        return ""