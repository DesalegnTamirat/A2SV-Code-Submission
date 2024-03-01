class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_letters = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        combinations = []
        letters = []
        def backtrack(i):
            if len(letters) == len(digits):
                combinations.append("".join(letters))
                return 
            
            for letter in digit_letters[digits[i]]:
                letters.append(letter)
                backtrack(i + 1)
                letters.pop()
            
        backtrack(0)
        return combinations