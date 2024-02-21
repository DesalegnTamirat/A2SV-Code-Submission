class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        
        prev_row = self.getRow(rowIndex - 1)
        ans = [1]
        for i in range(1, rowIndex):
            ans.append(prev_row[i - 1] + prev_row[i])
        ans.append(1)
        return ans

        