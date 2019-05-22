class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        ans = [0 for _ in range(len(num1) + len(num2))]
        position = len(ans) - 1
        for i in num1[::-1]:
            this_position = position
            for j in num2[::-1]:
                ans[this_position] += int(i) * int(j)
                ans[this_position - 1] += ans[this_position] / 10
                ans[this_position] %= 10
                
                this_position -= 1
            position -= 1
        
        index = 0
        while index < len(ans) - 1 and ans[index] == 0:
            index += 1
        
        return ''.join([str(element) for element in ans[index:]])