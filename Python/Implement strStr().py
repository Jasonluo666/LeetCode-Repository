class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        # compare the possible substring
        if not needle:
            return 0
        if not haystack:
            return -1
        
        needle_length = len(needle)
        haystack_length = len(haystack)
        
        for index in range(haystack_length):
            if index + needle_length > haystack_length:
                break
            
            if haystack[index] == needle[0] and haystack[index:index + needle_length] == needle:
                return index
        
        return -1