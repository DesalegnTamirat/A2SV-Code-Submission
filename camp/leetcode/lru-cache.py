class Node:
    
    def __init__(self, value=None,  next=None, prev=None):
        self.key = None
        self.value = value
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.caches = {}
        self.head = Node()
        self.tail = Node(prev=self.head)
        self.head.next = self.tail

    def get(self, key: int) -> int:
        if key in self.caches:
            node = self.caches[key]
            before = node.prev
            after = node.next
            before.next = after
            after.prev = before

            before = self.tail.prev
            node.next = self.tail
            node.prev = before 
            before.next = node
            self.tail.prev = node
            return node.value
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.caches:
            node = self.caches[key]
            node.value = value
            before = node.prev
            after = node.next
            before.next = after
            after.prev = before

            before = self.tail.prev
            node.next = self.tail
            node.prev = before 
            before.next = node
            self.tail.prev = node
            self.caches[key] = node
            return 
        if self.capacity == len(self.caches):
            self.caches.pop(self.head.next.key)
            after = self.head.next.next
            after.prev = self.head
            self.head.next = after
        
        node = Node(value = value)
        node.key = key
        before = self.tail.prev
        node.next = self.tail
        node.prev = before 
        before.next = node
        self.tail.prev = node
        self.caches[key] = node



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)