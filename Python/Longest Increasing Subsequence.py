class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        # DP problem -> dp[i] represent the maximum length till point i
        dp_table = [1 for _ in range(len(nums))]
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp_table[i] = max(dp_table[i], dp_table[j] + 1)
        
        
        
        return max(dp_table)