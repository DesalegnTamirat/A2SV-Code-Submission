class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        opens = 0
        for per in s:
            if per == ")" and opens == 0:
                count += 1
            elif per == ")":
                opens -= 1
            else:
                opens += 1
        
        return count + opens