class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def days_taken(weights, capacity):
            taken = 0
            total = 0
            for i, weight in enumerate(weights):
                total += weight
                if total >= capacity:
                    taken += 1
                    if total > capacity:
                        total = weight
                    else:
                        total = 0
                    
            
            return taken + 1 if total else taken
                
                

        left = max(weights)
        right = sum(weights)
        while left <= right:
            middle = left + (right - left) // 2
            taken = days_taken(weights, middle)
            if taken <= days:
                answer = middle
                right = middle - 1
            else:
                left = middle + 1
            
        return answer
