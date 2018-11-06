class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # multiply the left side and right side once -> O(n)
        left_multiply = 1
        right_multiply = 1
        ans = [1 for x in range(len(nums))]
        
        for index in range(len(nums)):
            ans[index] *= left_multiply
            ans[len(nums)-index-1] *= right_multiply
            left_multiply *= nums[index]
            right_multiply *= nums[len(nums)-index-1]
        
        return ans