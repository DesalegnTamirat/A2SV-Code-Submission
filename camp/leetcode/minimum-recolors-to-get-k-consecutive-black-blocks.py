class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        whites = blocks[:k].count("W")
        minimum = whites
        start = 1
        end = k
        while end < len(blocks):
            if blocks[start - 1] == "W":
                whites -= 1
            if blocks[end] == "W":
                whites += 1
            minimum = min(minimum, whites)
            start += 1
            end += 1

        return minimum

        