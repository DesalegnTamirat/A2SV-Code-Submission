class RecentCounter(object):

    def __init__(self):
        self.recents = []
        self.start = 0
        self.n = 0


    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        while self.start < self.n and t - self.recents[self.start] > 3000:
            self.start += 1
        
        self.recents.append(t)
        self.n += 1
        return self.n - self.start


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)