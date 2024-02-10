class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_repr = "".join(map(str, digits))
        plus_one = str(int(str_repr) + 1)
        return list(map(int, plus_one))