class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i = 0
        j = 0
        child = 0
        while i < len(g) and j < len(s):
            print(g[i], s[j])
            if g[i] <= s[j]:
                child += 1
                i += 1
                j += 1
            else:
                j += 1
        
        return child
            
