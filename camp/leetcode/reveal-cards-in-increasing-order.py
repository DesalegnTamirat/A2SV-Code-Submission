class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort()
        queue = deque()
        for i in range(-1, -len(deck) - 1, -1):
            if queue:
                popped = queue.popleft()
                queue.append(popped)
            queue.append(deck[i])

        return list(queue)[::-1]
            
        