class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # simple if/else -> with multiple conditions
        num = 0
        len_s = len(s)
        for index in range(len_s):
            if s[index] == 'M':
                num += 1000
            elif s[index] == 'D':
                num += 500
            elif s[index] == 'C':
                if index + 1 < len_s and (s[index + 1] == 'D' or s[index + 1] == 'M'):
                    num -= 100
                else:
                    num += 100
            elif s[index] == 'L':
                num += 50
            elif s[index] == 'X':
                if index + 1 < len_s and (s[index + 1] == 'L' or s[index + 1] == 'C'):
                    num -= 10
                else:
                    num += 10
            elif s[index] == 'V':
                num += 5
            elif s[index] == 'I':
                if index + 1 < len_s and (s[index + 1] == 'V' or s[index + 1] == 'X'):
                    num -= 1
                else:
                    num += 1
            
        
        return num