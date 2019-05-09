class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        char_map = {}
        for index in range(0, 26):
            char_map[chr(ord('A') + index)] = index + 1
        
        ans = 0
        for char in s:
            ans = ans * 26 + char_map[char]
        return ans