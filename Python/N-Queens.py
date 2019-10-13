class Solution:
    def updateMap(self, currentmap, x, y, count, n):
        for i in range(n):
            currentmap[x][i] += count
            currentmap[i][y] += count
            
            if x - i >= 0 and y - i >= 0:
                currentmap[x - i][y - i] += count
            if x - i >= 0 and y + i < n:
                currentmap[x - i][y + i] += count
            if x + i < n and y - i >= 0:
                currentmap[x + i][y - i] += count
            if x + i < n and y + i < n:
                currentmap[x + i][y + i] += count
    
    def dfs(self, path, currentmap, n):
        if len(path) == n:
            self.ans.append(path)
            return
        for index in range(n):
            if currentmap[len(path)][index] == 0:
                self.updateMap(currentmap, len(path), index, 1, n)
                self.dfs(path + [index], currentmap, n)
                self.updateMap(currentmap, len(path), index, -1, n)
        
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.ans = []
        
        currentmap = [[0 for _ in range(n)] for _ in range(n)]
        self.dfs([], currentmap, n)
        
        boards = []
        for x in self.ans:
            board = []
            for queen_pos in x:
                board.append('.' * queen_pos + 'Q' + '.' * (n - queen_pos - 1))
            
            boards.append(board)
        return boards