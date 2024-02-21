class MyCircularQueue(object):

    def __init__(self, k):
        self.queue = [-1] * k
        self.capacity = k
        self.start = -1
        self.end = -1

    def enQueue(self, value):
        if self.isFull():
            return False
        if self.isEmpty():
            self.start = 0
            self.end = 0
        self.queue[self.end] = value
        self.end += 1
        if self.end == self.capacity:
            self.end = 0
        return True
        
    def deQueue(self):
        if self.isEmpty():
            return False
        
        self.queue[self.start] = -1
        self.start += 1
        if self.start == self.capacity:
            self.start = 0
        
        if self.start == self.end:
            self.start = self.end = -1
        return True

    def Front(self):
        if self.isEmpty():
            return -1
        return self.queue[self.start]

    def Rear(self):
        if self.isEmpty():
            return -1
        if self.end - 1 < 0:
            return self.queue[self.capacity - 1]
        return self.queue[self.end - 1]

    def isEmpty(self):
        if self.start == self.end and self.start == -1:
            return True
        return False

    def isFull(self):
        if self.start == self.end and self.start != -1:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()