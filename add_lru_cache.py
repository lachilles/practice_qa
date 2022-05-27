class LRUCache:

    def __init__(self, capacity):
        self.vals = dict()
        self.max_size = capacity

    def put(self, key, value):
        if key in self.vals:
            del self.vals[key]
            self.vals[key] = value
        else:
            if len(self.vals) < self.max_size:
                self.vals[key] = value
            else:
                del self.vals[list(self.vals)[0]]
                self.vals[key] = value

    def get(self, key):
        if key in self.vals:
            return self.vals[key]
        return None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)