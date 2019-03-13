class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        neighbors = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
        
        if not board:
            return
        
        len_x = len(board)
        len_y = len(board[0])
        for index_x in range(len_x):
            for index_y in range(len_y):
                counter = 0
                
                # check neighbors
                for neighbor in neighbors:
                    current_neighbor = [index_x + neighbor[0], index_y + neighbor[1]]
                    # boundary check
                    if current_neighbor[0] >= 0 and current_neighbor[0] < len_x and current_neighbor[1] >= 0 and current_neighbor[1] < len_y:
                        if board[current_neighbor[0]][current_neighbor[1]] == 1 or board[current_neighbor[0]][current_neighbor[1]] == -9 or board[current_neighbor[0]][current_neighbor[1]] == 11:
                            counter = counter + 1
                
                # update rules -> alive next turn +10, otherwise -10
                if counter == 3:
                    board[index_x][index_y] += 10
                elif counter < 2 or counter > 3:
                    board[index_x][index_y] -= 10
        
        for index_x in range(len_x):
            for index_y in range(len_y):
                if board[index_x][index_y] > 0:
                    board[index_x][index_y] = 1
                else:
                    board[index_x][index_y] = 0