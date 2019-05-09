class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.root = {}
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        
        pointer = self.root
        for char in word:
            if char in pointer:
                pointer = pointer[char]
            else:
                pointer[char] = {}
                pointer = pointer[char]
        pointer['*'] = True
        return

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        
        pointer = self.root
        for char in word:
            if char in pointer:
                pointer = pointer[char]
            else:
                return False
        
        if '*' in pointer:
            return True
        else:
            return False
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        
        pointer = self.root
        for char in prefix:
            if char in pointer:
                pointer = pointer[char]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)