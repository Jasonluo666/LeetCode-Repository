class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        if len(word) == 0:
            return True
        elif len(board) == 0:
            return False
        
        def dfs(word, x, y):
            if len(word) == 0:
                return True
            if min(x, y) < 0 or x >= len(board) or y >= len(board[0]) or board[x][y] == '#':
                return False
            
            # not need for searching map -> put the # mark on the board and then return the value back after dfs
            if board[x][y] == word[0]:
                temp = board[x][y]
                # # mark
                board[x][y] = '#'
                
                ans = dfs(word[1:], x - 1, y) or dfs(word[1:], x + 1, y) or dfs(word[1:], x, y - 1) or dfs(word[1:], x, y + 1)
                
                # return the original board[x][y]
                board[x][y] = temp
                return ans
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == word[0]:
                    if dfs(word, x, y) == True:
                        return True
        
        return False