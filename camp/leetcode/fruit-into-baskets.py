class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        types = {}
        maximum = 0
        left = 0
        for right in range(len(fruits)):
            while len(types) == 2 and fruits[right] not in types:
                types[fruits[left]] -= 1
                if types[fruits[left]] == 0:
                    types.pop(fruits[left])
                left += 1
            types[fruits[right]] = types.get(fruits[right], 0) + 1
            maximum = max(maximum, right - left + 1)
        
        return maximum