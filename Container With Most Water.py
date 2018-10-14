class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        # O(N) -> greedy method
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            min_element = min(height[left], height[right])
            max_area = max(max_area, min_element * (right - left))
            
            if min_element == height[left]:
                left += 1
            else:
                right -= 1
        
        return max_area
        
        """
        # O(n^2) with pruning
        max_area = 0
        length = len(height)
        for index in range(length):
            max_limit = height[index] * (length - index - 1)
            if max_area > max_limit:
                continue
            
            for other_index in range(1, length - index):
                width = length - index - other_index
                if max_area > height[index] * width:
                    break
                
                area = min(height[index], height[-other_index]) * width
                if area > max_area:
                    max_area = area
        
        return max_area
        """