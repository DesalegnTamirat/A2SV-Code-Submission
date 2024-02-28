class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # sum of all pairs
        pair_sum = []
        n = len(weights)
        for i in range(1, n):
            pair_sum.append(weights[i] + weights[i - 1])
        
        # finding k - 1 most minimum and k - 1 most maximum
        # storing the sum of pairs on maximum and minimum
        pair_sum.sort()
        maximum = 0
        minimum = 0
        for i in range(1, k):
            maximum += pair_sum[-i]
            minimum += pair_sum[i - 1]
        
        return maximum - minimum
