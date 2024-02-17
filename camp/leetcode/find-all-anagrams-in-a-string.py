class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = Counter(p)
        k = len(p)
        current_window = Counter(s[:k])
        ans = []
        for i in range(len(s) - k + 1):
            if i != 0:
                current_window[s[i + k - 1]] = current_window.get(s[i + k - 1], 0) + 1
                if current_window[s[i - 1]] == 1:
                    current_window.pop(s[i - 1])
                else:
                    current_window[s[i - 1]] -= 1
            
            for letter in target:
                if letter not in current_window or target[letter] != current_window[letter]:
                    break
            else:
                if len(target) == len(current_window):
                    ans.append(i)

        return ans
            