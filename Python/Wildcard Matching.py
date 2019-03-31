class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # cache the existing result
        global cache
        cache = {}
        
        # recursive function -> explore all possible situations
        def recursive(s, p):
            # return cache value
            if (s, p) in cache.keys():
                return cache[(s, p)]
            
            # finish the pairing process
            if len(s) == 0 or len(p) == 0:
                index = 0
                for element in p:
                    if element == '*':
                        index += 1
                    else:
                        break
                
                if len(s) == 0 and len(p[index:]) == 0:
                    cache[(s, p)] = True
                    return True
                else:
                    cache[(s, p)] = False
                    return False
            
            # three situations: character, ?, *
            if p[0].isalpha() and p[0] == s[0]:
                cache[(s, p)] = recursive(s[1:], p[1:])
                return cache[(s, p)]
            elif p[0] == '?':
                cache[(s, p)] = recursive(s[1:], p[1:])
                return cache[(s, p)]
            elif p[0] == '*':
                index = 0
                for element in p:
                    if element == '*':
                        index += 1
                    else:
                        break
                
                cache[(s, p)] = recursive(s, p[index:]) or recursive(s[1:], p[index - 1:])
                return cache[(s, p)]
            else:
                cache[(s, p)] = False
                return False
        
        return recursive(s, p)