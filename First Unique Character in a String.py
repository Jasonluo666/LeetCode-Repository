class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        import collections
        # hash table -> count frequency
        hash_table = collections.Counter(s)
        
        for index in range(len(s)):
            if hash_table[s[index]] == 1:
                return index
        return -1