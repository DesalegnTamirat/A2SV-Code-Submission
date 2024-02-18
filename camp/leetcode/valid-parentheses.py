class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        for c in s:
            if c in ["(", "{", "["]:
                stack.append(c)
            else:
                if not stack:
                    return False
                r = stack.pop()

                if (r ==  "(" and c != ")") or (r == "[" and c != "]") or (r == "{" and c != "}"):
                    return False

        return not stack
        