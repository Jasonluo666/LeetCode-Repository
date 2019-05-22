class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        index = len(digits) - 1
        carry = 1
        while index >= 0:
            digits[index] += carry
            carry = int(digits[index] / 10)
            digits[index] %= 10
            
            if carry == 0:
                break
            
            index -= 1
        
        if carry > 0:
            digits = [carry] + digits
        
        return digits    