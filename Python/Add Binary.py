class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        a, b = a[::-1], b[::-1]
        if len(a) > len(b):
            a, b = b, a
        carry = 0
        ans = ""
        index = 0
        while index < len(a):
            pos = carry + int(a[index]) + int(b[index])
            carry = int(pos / 2)
            ans += str(pos % 2)
            index += 1
        
        while index < len(b):
            pos = carry + int(b[index])
            carry = int(pos / 2)
            ans += str(pos % 2)
            index += 1
        
        if carry == 1:
            ans += '1'
        
        return ans[::-1]