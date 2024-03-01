class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        deviates = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                deviates += 1

        return deviates