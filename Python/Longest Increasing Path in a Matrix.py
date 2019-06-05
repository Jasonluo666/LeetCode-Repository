class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
        global cache
        cache = {}
        
        def dfs(matrix, x, y, lastVal=None):
            global cache
            if not 0 <= x < len(matrix) or not 0 <= y < len(matrix[0]):
                return 0
            
            if (x, y, lastVal) in cache:
                return cache[(x, y, lastVal)]
            
            if lastVal is None or lastVal < matrix[x][y]:
                if (x - 1, y, matrix[x][y]) not in cache:
                    cache[(x - 1, y, matrix[x][y])] = dfs(matrix, x - 1, y, matrix[x][y])
                if (x + 1, y, matrix[x][y]) not in cache:
                    cache[(x + 1, y, matrix[x][y])] = dfs(matrix, x + 1, y, matrix[x][y])
                if (x, y - 1, matrix[x][y]) not in cache:
                    cache[(x, y - 1, matrix[x][y])] = dfs(matrix, x, y - 1, matrix[x][y])
                if (x, y + 1, matrix[x][y]) not in cache:
                    cache[(x, y + 1, matrix[x][y])] = dfs(matrix, x, y + 1, matrix[x][y])
                
                cache[(x, y, lastVal)] = 1 + max(cache[(x - 1, y, matrix[x][y])], cache[(x + 1, y, matrix[x][y])], cache[(x, y - 1, matrix[x][y])], cache[(x, y + 1, matrix[x][y])])
                
                return cache[(x, y, lastVal)]
            else:
                return 0
        
        ans = 0
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                cache[(x, y, None)] = dfs(matrix, x, y)
                ans = max(ans, cache[(x, y, None)])
        return ans