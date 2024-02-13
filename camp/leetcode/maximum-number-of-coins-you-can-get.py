class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = 1)
        # 1, 2, 2, 4, 7, 8
        i = 1
        ans = 0
        while i < len(piles) * 2 // 3:
            ans += piles[i]
            i += 2
        
        return ans
