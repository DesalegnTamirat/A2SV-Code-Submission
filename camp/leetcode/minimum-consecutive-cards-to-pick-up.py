class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        count = 0
        card_set = set()
        minimum = float("inf")
        left = 0
        for card in cards:
            while card in card_set:
                minimum = min(minimum, count + 1)
                count -= 1
                card_set.remove(cards[left])
                left += 1
            card_set.add(card)
            count += 1

        return -1 if minimum == float("inf") else minimum
        