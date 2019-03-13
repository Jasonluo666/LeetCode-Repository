class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        if not nums:
            return
        
        # set a pointer to record the first place to be swapped
        # put 0 in order
        empty_pos = 0
        for index in range(len(nums)):
            if nums[index] == 0:
                temp = nums[empty_pos]
                nums[empty_pos] = nums[index]
                nums[index] = temp
                empty_pos += 1
        
        # put 1 in order
        for index in range(empty_pos, len(nums)):
            if nums[index] == 1:
                temp = nums[empty_pos]
                nums[empty_pos] = nums[index]
                nums[index] = temp
                empty_pos += 1