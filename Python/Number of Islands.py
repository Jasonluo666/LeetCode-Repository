class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or len(grid) == 0:
            return 0
        
        count = 0
        
        def floodFill(x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == '0':
                return
            
            grid[x][y] = '0'
            floodFill(x - 1, y)
            floodFill(x + 1, y)
            floodFill(x, y - 1)
            floodFill(x, y + 1)
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    count += 1
                    floodFill(x, y)
        
        return count