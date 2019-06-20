class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        
        dp = [x for x in nums]
        dp[1] = max(dp[0], dp[1])
        for index in range(2, len(nums)):
            dp[index] = max(dp[index] + dp[index - 2], dp[index - 1])
        
        return dp[-1]