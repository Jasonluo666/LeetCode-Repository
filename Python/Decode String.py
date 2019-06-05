class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        ans = ""
        self.index = 0
        def recursive(s, n):
            this_str = ''
            
            while self.index < len(s):
                if s[self.index].isdigit():
                    time = ''
                    while s[self.index].isdigit():
                        time += s[self.index]
                        self.index += 1
                    
                    self.index += 1
                    this_str += recursive(s, int(time))
                elif s[self.index] == ']':
                    self.index += 1
                    return ''.join([this_str] * n)
                else:
                    this_str += s[self.index]
                    self.index += 1
            return ''.join([this_str] * n)
        
        return recursive(s, 1)