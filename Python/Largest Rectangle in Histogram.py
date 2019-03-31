class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        if len(heights) == 0:
            return ans
        
        # stack -> record the acsending pos
        heights.append(0)
        heights.insert(0,0)
        stack = []
        for index in range(len(heights)):
            # pop every larger element -> for stack[i], element between stack[i - 1], stack[i] is above heights[stack[i]]. otherwise it should remain in the stack as stack[i - 1]
            while len(stack) > 0 and heights[index] < heights[stack[-1]]:
                pos = stack.pop()
                area = heights[pos] * (index - stack[-1] - 1)
                ans = max(ans, area)
            stack.append(index)
        
        return ans