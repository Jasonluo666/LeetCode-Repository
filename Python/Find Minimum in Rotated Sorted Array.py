class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        
        for index in range(1, len(nums)):
            if nums[index] < nums[index - 1]:
                return nums[index]
        return nums[0]