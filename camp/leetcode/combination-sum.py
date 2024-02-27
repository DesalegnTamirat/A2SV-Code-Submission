class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        comb = []
        def backtrack(i):
            if sum(comb) == target:
                combinations.append(comb.copy())
                return 
            elif sum(comb) > target:
                return
            elif i == len(candidates):
                return 
            
            comb.append(candidates[i])
            backtrack(i)
            comb.remove(candidates[i])
            backtrack(i + 1)

        backtrack(0)
        return combinations