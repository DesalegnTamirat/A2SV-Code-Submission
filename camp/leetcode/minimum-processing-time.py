class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse = True)
        minimum = float("-inf")
        i = 0
        j = 0
        print(processorTime)
        print(tasks)
        for i in range(len(processorTime)):
            minimum = max(tasks[j] + processorTime[i], minimum)
            j += 4
        
        return minimum