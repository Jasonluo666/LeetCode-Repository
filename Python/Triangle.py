class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        dp = []
        for level in range(len(triangle)):
            dp.append([])
            for index in range(level + 1):
                x1, x2 = index, index - 1
                cost = triangle[level][index]
                
                if level == 0:
                    dp[-1].append(cost)
                elif x1 == level:
                    dp[-1].append(cost + dp[level - 1][x2])
                elif x2 < 0:
                    dp[-1].append(cost + dp[level - 1][x1])
                else:
                    dp[-1].append(cost + min(dp[level - 1][x1], dp[level - 1][x2]))
        
        return min(dp[-1])