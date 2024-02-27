class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        combination = []
        def backtrack(i):
            if len(combination) == k:
                combinations.append(combination.copy())
                return 
            elif i == n + 1 or len(combination) + n - i + 1 < k:
                return
            
            combination.append(i)
            backtrack(i + 1)
            combination.pop()
            backtrack(i + 1)
        
        backtrack(1)
        return combinations


            
        
        