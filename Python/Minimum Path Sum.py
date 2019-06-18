class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        dp[0][0] = grid[0][0]
        
        for x in range(1, len(grid)):
            dp[x][0] = dp[x - 1][0] + grid[x][0]
        
        for y in range(1, len(grid[0])):
            dp[0][y] = dp[0][y - 1] + grid[0][y]
        
        for x in range(1, len(grid)):
            for y in range(1, len(grid[0])):
                dp[x][y] = min(dp[x - 1][y], dp[x][y - 1]) + grid[x][y]
        
        return dp[-1][-1]