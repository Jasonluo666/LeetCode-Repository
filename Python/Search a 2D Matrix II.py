class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        # simply brute force search + condition limitations
        if not matrix:
            return False
        
        len_x = len(matrix)
        len_y = len(matrix[0])
        
        if len_y == 0:
            return False
        
        for index_x in range(len_x):
            if matrix[index_x][0] <= target <= matrix[index_x][len_y - 1]:
                for index_y in range(len_y):
                    if matrix[index_x][index_y] == target:
                        return True
        return False
        
        # BFS will cost more time in this case
        '''
        search_array = [(0,0)]
        while len(search_array) > 0:
            current_point = search_array[0]
            search_array = search_array[1:]
            
            if current_point[0] < len_x and current_point[1] < len_y:
                if matrix[current_point[0]][current_point[1]] == target:
                    return True
                elif matrix[current_point[0]][current_point[1]] < target:
                    search_array.append((current_point[0] + 1, current_point[1]))
                    search_array.append((current_point[0], current_point[1] + 1))
        return False
        '''
        