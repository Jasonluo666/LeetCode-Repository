class Solution:
    global cache
    cache = {}
    def isMatch(self, s: str, p: str) -> bool:
        global cache
        if (s, p) in cache.keys():
            return cache[(s, p)]
        
        if len(s) == 0 or len(p) == 0:
            previous_p = p
            while len(p) >= 2:
                if p[1] == '*':
                    p = p[2:]
                else:
                    break
            if len(s) == 0 and len(p) == 0:
                cache[(s, previous_p)] = True
                return True
            else:
                cache[(s, previous_p)] = False
                return False
        
        while len(p) >= 4 and p[1] == '*' and p[3] == '*':
            if p[0] == p[1]:
                p = p[2:]
            elif p[0] == '.' or p[2] == '.':
                p = '.' + p[3:]
            else:
                break
        
        if len(p) >= 2 and p[1] == '*':
            if p[0] == s[0] or p[0] == '.':
                cache[(s, p)] = self.isMatch(s, p[2:]) or self.isMatch(s[1:], p)
                return cache[(s, p)]
            else:
                cache[(s, p)] = self.isMatch(s, p[2:])
                return cache[(s, p)]
        elif p[0] == s[0] or p[0] == '.':
            cache[(s, p)] = self.isMatch(s[1:], p[1:])
            return cache[(s, p)]
        else:
            cache[(s, p)] = False
            return False
            
        