class Solution(object):
    def partitionLabels(self, s):
        letter_end = {}
        for i, letter in enumerate(s):
            letter_end[letter] = i
        
        ans = []
        elements = 0
        end = 0
        for i, letter in enumerate(s):
            elements += 1
            if end == i and i == letter_end[letter]:
                ans.append(elements)
                elements = 0
                end = i + 1
            elif end < letter_end[letter]:
                end = letter_end[letter]
        if elements != 0:
            ans.append(elements)
        return ans
            

            
        
        