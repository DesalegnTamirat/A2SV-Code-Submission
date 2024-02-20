class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minimums = []


    def push(self, val):
        self.stack.append(val)
        if not self.minimums or val <= self.minimums[-1]:
            self.minimums.append(val)
        

    def pop(self):
        removed = self.stack.pop()
        if removed == self.minimums[-1]:
            self.minimums.pop()
        

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.minimums[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()