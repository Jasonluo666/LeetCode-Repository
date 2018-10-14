class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        number = 0
        Upper_bound = 2 ** 31 - 1
        Lower_bound = -2 ** 31
        sign = None
        digit_flag = False
        
        for index in range(len(str)):
            if str[index] == ' ' and digit_flag == False and sign == None:
                pass
            elif (str[index] == '+' or str[index] == '-') and sign == None and digit_flag == False:
                sign = str[index]
            else:
                if str[index].isdigit():
                    digit_flag = True
                    
                    number = number * 10 + int(str[index])
                    
                    if number > Upper_bound:
                        if sign == '-':
                            return Lower_bound
                        else:
                            return Upper_bound
                else:
                    if digit_flag:
                        break
                    else:
                        return 0
        
        if sign == '-':
            return -number
        else:
            return number
            