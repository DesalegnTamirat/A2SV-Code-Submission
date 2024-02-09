class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        range_sum = [0 for _ in range(n + 1)]
        for first, last, seats in bookings:
            range_sum[first] += seats
            if last != n:
                range_sum[last + 1] -= seats

        prefix_sum = []
        for seats in range_sum[1:]:
            if prefix_sum:
                prefix_sum.append(prefix_sum[-1] + seats)
            else:
                prefix_sum.append(seats)

        return prefix_sum


        