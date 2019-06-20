class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        
        dp = [[0 for _ in matrix[0]] for _ in matrix]
        ans = 0
        
        for x in range(len(matrix)):
            dp[x][0] = int(matrix[x][0])
            ans = max(ans, dp[x][0])
        for y in range(len(matrix[0])):
            dp[0][y] = int(matrix[0][y])
            ans = max(ans, dp[0][y])
        
        for x in range(1, len(matrix)):
            for y in range(1, len(matrix[0])):
                if matrix[x][y] == '1':
                    prev_x, prev_y = x, y
                    while prev_x - 1 >= 0 and matrix[prev_x - 1][y] == '1':
                        prev_x -= 1
                    while prev_y - 1 >= 0 and matrix[x][prev_y - 1] == '1':
                        prev_y -= 1

                    dp[x][y] = min(x - prev_x, y - prev_y, dp[x - 1][y - 1]) + 1
                    ans = max(ans, dp[x][y])
        
        return ans ** 2