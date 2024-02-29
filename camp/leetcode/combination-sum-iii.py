class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        answer = []
        path = []
        def backtrack(num, total):
            if total == n and len(path) == k:
                answer.append(path.copy())
                return
            if len(path) == k or num > 9:
                return

            # include
            path.append(num)
            backtrack(num + 1, total + num)
            path.pop()
            # don't include
            backtrack(num + 1, total)
        
        backtrack(1, 0)
        return answer