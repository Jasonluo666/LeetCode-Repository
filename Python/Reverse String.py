class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        reverse_str = ''
        for index in range(1, len(s) + 1):
            reverse_str += s[-index]
        
        return reverse_str