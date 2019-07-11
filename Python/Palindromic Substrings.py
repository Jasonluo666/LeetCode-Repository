class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        index = 0
        ans = 0
        while index < len(s):
            shift = 0
            while 0 <= index - shift <= index + shift < len(s):
                if s[index - shift] == s[index + shift]:
                    ans += 1
                    shift += 1
                else:
                    break
            
            shift = 0
            neighbor = index + 1
            while 0 <= index - shift <= neighbor + shift < len(s):
                if s[index - shift] == s[neighbor + shift]:
                    ans += 1
                    shift += 1
                else:
                    break
            index += 1
        
        return ans