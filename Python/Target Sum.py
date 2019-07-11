class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.cache = {}
        
        def dfs(nums, index, ans, S):
            if index == len(nums):
                if ans == S:
                    return 1
                else:
                    return 0
            
            if (index, ans) in self.cache:
                return self.cache[(index, ans)]
            
            self.cache[(index, ans)] = dfs(nums, index + 1, ans + nums[index], S) + dfs(nums, index + 1, ans - nums[index], S)
            return self.cache[(index, ans)]
        
        return dfs(nums, 0, 0, S)