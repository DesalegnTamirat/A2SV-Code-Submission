class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        time = 0
        for i, ticket in enumerate(tickets):
            time += min(tickets[k], ticket)
            if ticket >= tickets[k] and i > k:
                time -= 1
        
        return time
