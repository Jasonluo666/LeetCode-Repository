class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        if not board:
            return
        
        # hash table -> check each row/col/box
        row = [{} for x in range(9)]
        col = [{} for x in range(9)]
        box = [{} for x in range(9)]
        
        len_x = len(board)
        len_y = len(board[0])
        
        for index_x in range(len_x):
            for index_y in range(len_y):
                if board[index_x][index_y] != '.':
                    if board[index_x][index_y] not in row[index_x].keys():
                        row[index_x][board[index_x][index_y]] = True
                    else:
                        return False

                    if board[index_x][index_y] not in col[index_y].keys():
                        col[index_y][board[index_x][index_y]] = True
                    else:
                        return False

                    box_index = int(index_x / 3) * 3 + int(index_y / 3)
                    if board[index_x][index_y] not in box[box_index].keys():
                        box[box_index][board[index_x][index_y]] = True
                    else:
                        return False
        
        return True