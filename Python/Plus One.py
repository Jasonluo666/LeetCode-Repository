class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits) - 1
        carry = True
        
        while carry == True and index > -1:
            carry = False
            digits[index] += 1
            
            if digits[index] == 10:
                digits[index] = 0
                carry = True
            
            index -= 1
        
        if carry == True:
            digits = [1] + digits
        
        return digits