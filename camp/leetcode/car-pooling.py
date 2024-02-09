class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passengers = [0 for i in range(1001)]
        for num_passengers, start, end in trips:
            passengers[start] += num_passengers
            passengers[end] -= num_passengers

        total_count = 0
        for num_passengers in passengers:
            total_count += num_passengers
            if total_count > capacity:
                return False

        return True