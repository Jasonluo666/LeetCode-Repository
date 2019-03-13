class Solution:
    def calculate(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        if not s[0].isdigit():
            s = s[1:]
        
        # stack operations + prioritize the orders + "+/-" oeprations
        stack = []
        num = None
        for element in s:
            if element.isdigit():
                if num is None:
                    num = element
                else:
                    num += element
            elif element in '+-*/':
                if len(stack) == 0:
                    stack.append(int(num))
                    stack.append(element)
                elif stack[-1] in '*/' or element in '+-':
                    opr = stack.pop()
                    if opr in '+-':
                        if len(stack) > 1:
                            if stack[-2] == opr:
                                stack[-1] = stack[-1] + int(num)
                            else:
                                stack[-1] = stack[-1] - int(num)
                        else:
                            if opr == '+':
                                stack[-1] = stack[-1] + int(num)
                            else:
                                stack[-1] = stack[-1] - int(num)
                    elif opr == '-':
                        stack[-1] = stack[-1] - int(num)
                    elif opr == '*':
                        stack[-1] = stack[-1] * int(num)
                    elif opr == '/':
                        stack[-1] = int(stack[-1] / int(num))
                    
                    stack.append(element)
                else:
                    stack.append(int(num))
                    stack.append(element)
                num = None
                
        if num is not None:
            stack.append(int(num))
            while len(stack) > 1:
                num2 = stack.pop()
                opr = stack.pop()
                if opr in '+-':
                    if len(stack) > 1:
                        if stack[-2] == opr:
                            stack[-1] = stack[-1] + num2
                        else:
                            stack[-1] = stack[-1] - num2
                    else:
                        if opr == '+':
                            stack[-1] = stack[-1] + num2
                        else:
                            stack[-1] = stack[-1] - num2
                elif opr == '*':
                    stack[-1] = stack[-1] * num2
                elif opr == '/':
                    stack[-1] = int(stack[-1] / num2)
                
        return stack[-1]