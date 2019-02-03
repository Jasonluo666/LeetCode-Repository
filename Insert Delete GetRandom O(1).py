class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_table = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.hash_table.keys():
            self.hash_table[val] = True
            return True
        
        return False
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.hash_table.keys():
            del self.hash_table[val]
            return True
        
        return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random
        
        ran_num = random.randint(0, len(self.hash_table.keys()) - 1)
        return list(self.hash_table.keys())[ran_num]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()