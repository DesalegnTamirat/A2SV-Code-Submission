class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = list(map(str, nums))
        
        def compare(num1, num2):
            if num1 + num2 > num2 + num1:
                return -1
            return 1

        return str(int("".join(sorted(strs, key = cmp_to_key(compare)))))