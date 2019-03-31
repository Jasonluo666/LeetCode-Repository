class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        
        # two pointers + two local max
        ans = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        while left < right:
            if height[left] < height[right]:
                if height[left] < left_max:
                    ans += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1
            else:
                if height[right] < right_max:
                    ans += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1
        
        return ans