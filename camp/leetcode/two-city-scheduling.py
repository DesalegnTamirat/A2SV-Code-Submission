class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda cost: abs(cost[0] - cost[1]), reverse = True)
        total_cost = 0
        a = 0
        b = 0
        for a_cost, b_cost in costs:
            if a == len(costs) // 2:
                total_cost += b_cost
                b += 1
            elif b == len(costs) // 2:
                total_cost += a_cost
                a += 1
            elif a_cost < b_cost:
                total_cost += a_cost
                a += 1
            else:
                total_cost += b_cost
                b += 1
        
        return total_cost


