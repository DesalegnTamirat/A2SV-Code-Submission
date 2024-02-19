class Solution(object):
    def scoreOfParentheses(self, s):
        stack = []
        score = 0
        for par in s:
            if par == "(":
                stack.append(score)
                score = 0
            else:
                score = stack.pop() + max(2 * score, 1)
        
        return score

        