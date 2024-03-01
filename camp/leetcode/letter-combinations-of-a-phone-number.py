class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_letters = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        
        possibilities = []
        for digit in digits:
            possibilities.append(digit_letters[digit])
        
        answer = []
        path = []
        def backtrack(i):
            if len(path) == len(digits):
                answer.append("".join(path))
                return
            if i == len(possibilities):
                return

            for let in possibilities[i]:
                path.append(let)
                backtrack(i + 1)
                path.pop()
                backtrack(i + 1)
            
        backtrack(0)
        return answer
