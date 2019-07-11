class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        
        ans = [0 for x in T]
        stack = []
        for index, element in enumerate(T):
            while len(stack) > 0 and stack[-1][1] < element:
                prev = stack.pop()
                ans[prev[0]] = index - prev[0]
            
            stack.append((index, element))
        return ans