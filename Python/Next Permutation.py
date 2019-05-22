class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        if not nums:
            return
        
        index = len(nums) - 2
        while index >= 0:
            # find the reverse point
            if nums[index] < nums[index + 1]:
                break
            index -= 1
        
        # reverse entire list
        if index == -1:
            nums[:] = nums[::-1]
        else:
            # reverse the sub list
            nums[index + 1:] = nums[index + 1:][::-1]
            
            # swap the current point with the smallest larger element in sub list
            next_index = index + 1
            while next_index < len(nums):
                if nums[next_index] > nums[index]:
                    nums[index], nums[next_index] = nums[next_index], nums[index]
                    break
                next_index += 1
        
        return