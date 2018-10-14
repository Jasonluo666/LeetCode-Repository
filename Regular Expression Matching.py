cache={}

class Solution:
    '''def __init__(self):
        self.cache={}'''
        
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        # time -> space
        global cache
        
        # if have computed before, return the answer
        if (s,p) in cache:
            return cache[(s,p)]
        
        # end of matching
        if len(s) == 0 or len(p) == 0:
            if len(s) == 0 and len(p) == 0:
                return True
            elif len(p) > 1 and p[1] == '*':
                if (s,p) not in cache:
                    cache[(s, p[2:])] = self.isMatch(s, p[2:])
                return cache[(s, p[2:])]
            else:
                return False
        
        # pruning
        while len(p) >= 4 and p[1] == p[3] == '*':
            if p[0] == p[2]:
                p = p[2:]
            elif p[0] == '.':
                p = '.' + p[3:]
            else:
                break
        
        # conditions with *
        if len(p) > 1 and p[1] == '*':
            if self.isMatch(s, p[2:]):
                cache[(s,p)] = True
                return cache[(s,p)]
            elif p[0] == s[0] or p[0] == '.':
                cache[(s[1:], p)] = self.isMatch(s[1:], p) 
                return cache[(s[1:], p)]
        
        # single pair
        if p[0] != s[0] and p[0] != '.':
            return False
        else:
            cache[(s[1:], p[1:])] = self.isMatch(s[1:], p[1:])
            return cache[(s[1:], p[1:])]