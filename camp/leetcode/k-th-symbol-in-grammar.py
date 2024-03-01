class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        answer = 0
        left, right = 1, 2 ** (n - 1)
        for _ in range(n):
            middle = (left + right) // 2
            if k <= middle:
                right = middle
            else:
                left = middle + 1
                answer = 1 if answer == 0 else 0

        return answer