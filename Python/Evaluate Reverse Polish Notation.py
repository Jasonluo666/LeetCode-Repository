class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 0:
            return 0
        
        # basic stack operation
        stack = []
        for element in tokens:
            if element not in '+-*/':
                stack.append(int(element))
            else:
                second_num = stack.pop()
                
                if element == '+':
                    stack[-1] += second_num
                elif element == '-':
                    stack[-1] -= second_num
                elif element == '*':
                    stack[-1] *= second_num
                elif element == '/':
                    stack[-1] = int(stack[-1] / second_num)
        
        return stack[-1]