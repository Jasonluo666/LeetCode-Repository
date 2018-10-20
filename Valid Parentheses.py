class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # simple stack operations
        stack = []
        flag = True
        
        for element in s:
            if element == '(' or element == '[' or element == '{':
                stack.append(element)
            else:
                if len(stack) > 0 and ((stack[-1] == '(' and element == ')') or (stack[-1] == '[' and element == ']') or (stack[-1] == '{' and element == '}')):
                    stack.pop(-1)
                else:
                    flag = False
                    break
        
        if len(stack) > 0:
            flag = False
        
        return flag