class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        left = right = 0
        while right < len(nums):
            if nums[right] == 0:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                left += 1
            right += 1
        
        right = left
        while right < len(nums):
            if nums[right] == 1:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                left += 1
            right += 1