class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        radiants = deque()
        dires = deque()
        for i, party in enumerate(senate):
            if party == "R":
                radiants.append(i)
            else:
                dires.append(i)

        i = 0
        n = len(senate)
        while radiants or dires:
            i = i % n
            party = senate[i]
            if party == "R" and radiants and radiants[0] == i:
                if not dires:
                    return "Radiant"
                else:
                    dires.popleft()
                    radiants.append(radiants.popleft())
            elif party == "D" and dires and dires[0] == i:
                if not radiants:
                    return "Dire"
                else:
                    radiants.popleft()
                    dires.append(dires.popleft())
            i += 1
            


        