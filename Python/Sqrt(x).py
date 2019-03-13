class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x == 1:
            return 1
        
        left, right = 0, x
        mid = int((left + right) / 2)
        
        while left < right:
            if mid ** 2 <= x < (mid + 1) ** 2:
                break
            
            if mid ** 2 > x:
                right = mid
            else:
                left = mid
            
            mid = int((left + right) / 2)
        
        return mid