class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        maximum = None
        minimum = None
        total = 0
        for value in salary:
            if maximum == None or value > maximum:
                maximum = value
            
            if minimum == None or value < minimum:
                minimum = value
            total += value

        return (total - minimum - maximum) / float(len(salary) - 2)
        