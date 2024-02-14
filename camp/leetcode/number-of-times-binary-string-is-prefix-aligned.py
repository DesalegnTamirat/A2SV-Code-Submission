class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        ans = right = 0
        for i in range(len(flips)):
            right = max(right, flips[i])
            if right == i + 1:
                ans += 1
        
        return ans
