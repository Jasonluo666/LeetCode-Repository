class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        ans = 0
        stack = []
        left = 0
        for index in range(len(s)):
            if s[index] == '(':
                stack.append(index)
            else:
                if not stack:
                    left = index + 1
                else:
                    stack.pop()
                    if not stack:
                        ans = max(ans, index - left + 1)
                    else:
                        ans = max(ans, index - stack[-1])
        return ans