class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters) - 1
        answers = []
        while left <= right:
            middle = (left + right) // 2
            answer = letters[middle]
            if answer > target:
                answers.append(answer)
                right = middle - 1
            else:
                left = middle + 1
        
        answers.sort()
        return answers[0] if answers else letters[0]