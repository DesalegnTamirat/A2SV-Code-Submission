class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter_s1 = Counter(s1)
        k = len(s1)
        counter_s2 = Counter(s2[:k])
        i = 0
        j = k - 1
        while True:
            for letter in counter_s1:
                if letter not in counter_s2 or counter_s1[letter] != counter_s2[letter]:
                    break
            else:
                return True
            
            i += 1
            j += 1
            if j >= len(s2):
                break
            counter_s2[s2[j]] = counter_s2.get(s2[j], 0) + 1
            counter_s2[s2[i - 1]] -= 1
            if counter_s2[s2[i - 1]] == 0:
                counter_s2.pop(s2[i - 1])
            
            
        return False
                