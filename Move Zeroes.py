class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        if not nums:
            return
        
        index = non_zero = 0
        while index < len(nums):
            if nums[index] != 0:
                temp = nums[index]
                nums[index] = nums[non_zero]
                nums[non_zero] = temp
                
                non_zero += 1
            
            index +=1
                    
