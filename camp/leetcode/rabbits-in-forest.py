class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        color_rabbitCount = {}
        rabbits = 0
        for answer in answers:
            if answer == 0:
                # only rabbit with that color
                rabbits += 1 
            elif answer not in color_rabbitCount or answer == color_rabbitCount[answer] - 1:
                # the rabbit itself and others it answered
                rabbits += answer + 1
                color_rabbitCount[answer] = 1
            else:
                color_rabbitCount[answer] += 1
        
        return rabbits

