class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        self.cache = {}
        
        def recursive(s, t, index_s, index_t):
            if not t[index_t:]:
                return 1
            
            if not s[index_s:]:
                return 0
            
            if (index_s, index_t) in self.cache:
                return self.cache[(index_s, index_t)]
            
            if s[index_s] == t[index_t]:
                ans = recursive(s, t, index_s + 1, index_t + 1) + recursive(s, t, index_s + 1, index_t)
            else:
                ans = recursive(s, t, index_s + 1, index_t)
            
            self.cache[(index_s, index_t)] = ans
            return ans
        
        return recursive(s, t, 0, 0)