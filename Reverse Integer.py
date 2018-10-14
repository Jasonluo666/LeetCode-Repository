class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        # easy to deal with strings
        x_str = str(x)
        x_reverse = ''
        symbol = '+'
        if len(x_str) > 0 and x_str[0] == '-':
            x_str = x_str[1:]
            symbol = '-'
        
        for index in range(len(x_str)):
            x_reverse = x_reverse + x_str[len(x_str) - index - 1]
        
        if symbol == '-':
            x_reverse = symbol + x_reverse
        
        num = float(x_reverse)
        if num > 2 ** 31 - 1 or num < -2 ** 31:
            return 0
        else:
            return int(x_reverse)