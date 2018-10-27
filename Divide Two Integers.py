class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        # use bisection, double the value (start from the divior) until the upper bound is found
        # equation: dividend = q * divisor + r
        
        # preprocessing -> flip the dividend and divisor to positive
        flag = True
        if dividend < 0:
            dividend = - dividend
            flag = not flag
        if divisor < 0:
            divisor = - divisor
            flag = not flag
        
        if dividend < divisor:
            return 0
        
        bisection = [(divisor, 1)]
        while True:
            leftover = dividend - bisection[-1][0]
            
            if leftover <= 0:
                break
            else:
                bisection.append((bisection[-1][0] + bisection[-1][0], bisection[-1][1] + bisection[-1][1]))
        
        if dividend - bisection[-1][0] == 0:
            q = bisection[-1][1]
        else:
            q = bisection[-2][1]
            r = dividend - bisection[-2][0]
            for element in bisection[::-1]:
                if element[0] <= r:
                    r -= element[0]
                    q += element[1]
        
        if not flag:
            q = -q
        if not (- 2 ** 31 <= q <= 2 ** 31 - 1):
            return 2 ** 31 - 1
        else:
            return q