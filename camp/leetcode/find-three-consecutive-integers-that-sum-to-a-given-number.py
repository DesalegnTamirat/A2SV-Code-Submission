class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        first = num // 3 - 1
        if first * 3 + 3 == num:
            return [first, first + 1, first + 2]
        else:
            return []