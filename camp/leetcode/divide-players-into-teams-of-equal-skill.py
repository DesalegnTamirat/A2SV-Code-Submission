class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i = 0
        j = len(skill) - 1
        total = 0
        prev = skill[i] + skill[j]
        while i < j:
            if skill[i] + skill[j] != prev:
                return -1
            total += skill[i] * skill[j]
            i += 1
            j -= 1
        
        return total
            