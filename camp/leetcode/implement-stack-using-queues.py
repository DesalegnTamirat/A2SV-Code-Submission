class MyStack(object):

    def __init__(self):
        self.stack = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: int
        """ 
        queue = deque()
        while len(self.stack) > 1:
            queue.append(self.stack.popleft())
        removed = self.stack.popleft()
        while queue:
            self.stack.append(queue.popleft())
        
        return removed
        

    def top(self):
        """
        :rtype: int
        """
        queue = deque()
        while len(self.stack) > 1:
            queue.append(self.stack.popleft())
        removed = self.stack.popleft()
        while queue:
            self.stack.append(queue.popleft())
        self.stack.append(removed)
        
        return removed
        

    def empty(self):
        """
        :rtype: bool
        """
        if self.stack:
            return False
        return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()