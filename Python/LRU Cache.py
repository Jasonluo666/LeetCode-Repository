class LRUCache:

    # use collections.OrderedDict
    def __init__(self, capacity: int):
        import collections
        self.data = collections.OrderedDict()
        self.capacity = capacity
        self.volume = 0

    def get(self, key: int) -> int:
        if key in self.data.keys():
            self.data.move_to_end(key)
            return self.data[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.data.keys():
            if self.volume == self.capacity:
                # remove the first element
                # p.s. remove the tail ->  self.data.popitem()
                self.data.popitem(last=False)
            else:
                self.volume += 1
        else:
            # change the order of dict element -> move to the tail
            self.data.move_to_end(key)
        
        self.data[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)