class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda cost: abs(cost[0] - cost[1]), reverse = True)
        total_cost = 0
        a = 0
        b = 0
        n = len(costs)
        for a_cost, b_cost in costs:
            if a == n // 2 or b != n // 2 and b_cost < a_cost:
                total_cost += b_cost
                b += 1
            else:
                total_cost += a_cost
                a += 1
        
        return total_cost


