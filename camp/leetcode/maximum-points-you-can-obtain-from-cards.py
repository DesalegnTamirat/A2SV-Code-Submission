class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)
        w = n - k
        total = minimum = sum(cardPoints[:w])
        start = 1
        end = w
        while end < n:
            total -= cardPoints[start - 1]
            total += cardPoints[end]
            minimum = min(minimum, total)
            start += 1
            end += 1
        return sum(cardPoints) - minimum


        