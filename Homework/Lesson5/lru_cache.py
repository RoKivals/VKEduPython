from collections import deque


class LRUCache:

    def __init__(self, limit=2):
        self.cache = deque(maxlen=limit)
        self.hash = dict()
        self.size = limit

    def full(self):
        return len(self.cache) == self.cache.maxlen

    def get(self, key):
        return self.hash.get(key, None)

    def set(self, key, value):
        if key not in self.hash:
            if self.full():
                self.hash.pop(self.cache[self.size][0])
                self.cache.pop()
            self.hash[key] = value
            self.cache.appendleft((key, value))

        else:
            self.cache.remove((key, value))
            self.cache.appendleft((key, value))
