class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return
        
        ans, current_max, current_min = nums[0], nums[0], nums[0]
        
        # DP problem
        for element in nums[1:]:
            # forward the local max/min
            current_max, current_min = max(current_max * element, current_min * element, element), min(current_max * element, current_min * element, element)
            
            ans = max(ans, current_max)
        
        return ans