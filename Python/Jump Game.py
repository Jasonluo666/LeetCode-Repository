class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        max_reach = 0
        index = 0
        while index <= max_reach and index < len(nums):
            jump = index + nums[index]
            if max_reach < jump:
                max_reach = jump
            index += 1
        
        if index == len(nums):
            return True
        else:
            return False