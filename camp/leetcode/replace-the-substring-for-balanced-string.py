class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        reptition = Counter(s)
        extra_char = {}
        for let in reptition:
            if reptition[let] > n // 4:
                extra_char[let] = reptition[let] - n // 4
        
        if not extra_char: # if extra_char empty then nothing to replace
            return 0

        left = 0
        minimum = float("inf")
        for right in range(n):
            if s[right] in extra_char:
                extra_char[s[right]] -= 1
            
            # move the left if all extras are in the substring
            while max(extra_char.values()) <= 0:
                minimum = min(minimum, right - left + 1)
                if s[left] in extra_char:
                    extra_char[s[left]] += 1
                left += 1
            
        return minimum