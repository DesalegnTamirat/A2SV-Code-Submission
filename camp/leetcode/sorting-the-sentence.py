class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        order_word = sorted([[word[-1], word[:-1]] for word in s.split()], key = lambda pair: pair[0])
        return " ".join([pair[1] for pair in order_word])
        