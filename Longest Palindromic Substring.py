class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # O(n^2) -> good readability
        max_length = 0
        pos1, pos2 = 0, 0
        
        # for each element, expend its neighbors on both sides, stop if non-matched neighbors are found
        for index in range(len(s)):
            odd_length = 1
            even_length = 0
            
            # odd
            index_left = index - 1
            index_right = index + 1
            while index_left >= 0 and index_right < len(s):
                if s[index_left] == s[index_right]:
                    odd_length += 2
                    index_left -= 1
                    index_right += 1
                else:
                    break
            
            length = index_right - index_left - 1
            if max_length < length:
                max_length = length
                pos1 = index_left + 1
                pos2 = index_right - 1
            
            # even
            index_left = index
            index_right = index + 1
            while index_left >=0 and index_right < len(s):
                if s[index_left] == s[index_right]:
                    even_length += 2
                    index_left -= 1
                    index_right += 1
                else:
                    break

            length = index_right - index_left - 1
            if max_length < length:
                max_length = length
                pos1 = index_left + 1
                pos2 = index_right - 1
        
        
        return s[pos1 : pos2 + 1]
            
            