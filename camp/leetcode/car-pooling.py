class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        range_sum = [0 for _ in range(1001)]
        for numPassengers, start, end in trips:
            range_sum[start] += numPassengers
            range_sum[end] -= numPassengers
        
        accumulator = 0
        for num in range_sum:
            accumulator += num
            if accumulator > capacity:
                return False
        
        return True
        