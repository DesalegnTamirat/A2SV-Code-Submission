class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        counts = [0] * (max(costs) +  1)
        for cost in costs:
            counts[cost] += 1
        
        print(counts)
        ice_creams = 0
        for i, count in enumerate(counts):
            if (coins - count * i) >= 0:
                coins -= count * i
                ice_creams += count
            else:
                return ice_creams + coins // i

        return ice_creams
