class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        self.cache = {}
        def recursive(s):
            if not s:
                return 1
            
            ans = 0
            if len(s) > 1 and 10 <= int(s[:2]) <= 26:
                if s[2:] in self.cache:
                    ans += self.cache[s[2:]]
                else:
                    self.cache[s[2:]] = recursive(s[2:])
                    ans += self.cache[s[2:]]
            
            if s[0] != '0':
                if s[1:] in self.cache:
                    ans += self.cache[s[1:]]
                else:
                    self.cache[s[1:]] = recursive(s[1:])
                    ans += self.cache[s[1:]]
            return ans
        
        return recursive(s)