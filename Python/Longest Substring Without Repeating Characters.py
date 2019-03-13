class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # O(n^2)
        if len(s) > 0:
            max_length = 1
        else:
            max_length = 0
        head_index = 0
        for index in range(1, len(s)):
            new_element = s[index]
            for sub_index in range(head_index, index):
                if s[sub_index] == new_element:
                    max_length = max(index - head_index, max_length)
                    head_index = sub_index + 1
                    break
            
            if index == len(s) - 1:
                max_length = max(index - head_index + 1, max_length)
        
        return max_length