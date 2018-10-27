class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # replace the redundant elements with the unique ones
        if not nums:
            return 0
        
        unique_element_index = 1
        for index in range(1, len(nums)):
            if nums[index] == nums[index - 1]:
                continue
            
            nums[unique_element_index] = nums[index]
            unique_element_index += 1
        
        return unique_element_index