class Solution(object):
    def reverseString(self, s, start=0, end=None):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        if end == None:
            end = len(s) - 1
        if start >= end:
            return s
        s[start], s[end] = s[end], s[start]
        return self.reverseString(s, start + 1, end - 1)
        
        