class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        boats = 0
        start = 0
        end = len(people) - 1
        while start <= end:
            weight = people[start] + people[end]
            if weight <= limit:
                boats += 1
                start += 1
                end -= 1
            else:
                boats += 1
                end -= 1
        
        return boats
            