class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        # binary search through the sorted list
        left, right = 0, len(nums)
        half = int((left + right) / 2)
        while nums[half] != target:
            if nums[half] < target:
                left = half
            else:
                right = half
            
            next_half = int((left + right) / 2)
            delta = next_half - half
            half = next_half
            if delta == 0:
                break
        
        # expand the neighbors with same value
        if nums[half] != target:
            return [-1, -1]
        else:
            left, right = half, half
            while left >= 0 and nums[left] == target:
                left -= 1
            
            while right < len(nums) and nums[right] == target:
                right += 1
            
            return [left + 1, right - 1]
            