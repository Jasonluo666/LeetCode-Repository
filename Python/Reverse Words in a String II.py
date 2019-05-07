class Solution(object):
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: None Do not return anything, modify str in-place instead.
        """
        
        str.reverse()
        left = right = 0
        while right < len(str):
            if not str[right] == ' ':
                right += 1
                continue
            
            self.reverse(str, left, right - 1)
            right += 1
            left = right
            
        self.reverse(str, left, right - 1)
    
    
    def reverse(self, str, left, right):
        while left < right:
            temp = str[left]
            str[left] = str[right]
            str[right] = temp
            left += 1
            right -= 1