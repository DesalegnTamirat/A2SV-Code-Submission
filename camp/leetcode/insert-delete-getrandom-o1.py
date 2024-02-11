from random import choice

class RandomizedSet:

    def __init__(self):
        self.container = {}
        self.elements = []
        self.length = 0

    def insert(self, val: int) -> bool:
        if val in self.container:
            return False

        self.elements.append(val)
        self.container[val] = self.length
        self.length += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.container:
            return False
        
        index = self.container[val]
        self.elements[index] = self.elements[self.length - 1]
        self.elements.pop()
        self.container.pop(val)
        self.length -= 1
        if index < self.length:
            self.container[self.elements[index]] = index
        return True

    def getRandom(self) -> int:
        return choice(self.elements)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()