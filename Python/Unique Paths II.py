class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or len(obstacleGrid) == 0 or obstacleGrid[0][0] == 1:
            return 0
        
        
        dp = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        for x in range(0, len(obstacleGrid)):
            if obstacleGrid[x][0] != 1:
                dp[x][0] = 1
            else:
                break
        
        for y in range(1, len(obstacleGrid[0])):
            if obstacleGrid[0][y] != 1:
                dp[0][y] = 1
            else:
                break
        
        for x in range(1, len(obstacleGrid)):
            for y in range(1, len(obstacleGrid[0])):
                if obstacleGrid[x][y] != 1:
                    dp[x][y] = dp[x - 1][y] + dp[x][y - 1]
        return dp[-1][-1]