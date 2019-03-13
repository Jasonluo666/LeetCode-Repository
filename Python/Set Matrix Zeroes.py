class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        # mark the zeros
        import numpy as np
        
        if not matrix:
            return
        len_x = len(matrix)
        len_y = len(matrix[0])
        def set(x, y):
            for index in range(len_x):
                if matrix[index][y] == 0 or matrix[index][y] == np.inf:
                    matrix[index][y] = np.inf
                else:
                    matrix[index][y] = -np.inf
            for index in range(len_y):
                if matrix[x][index] == 0 or matrix[x][index] == np.inf:
                    matrix[x][index] = np.inf
                else:
                    matrix[x][index] = -np.inf
            
        
        for x in range(len_x):
            for y in range(len_y):
                if matrix[x][y] == 0 or matrix[x][y] == np.inf:
                    set(x, y)
        
        for x in range(len_x):
            for y in range(len_y):
                if np.abs(matrix[x][y]) == np.inf:
                    matrix[x][y] = 0