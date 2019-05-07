class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if not matrix or len(matrix[0]) == 0:
            return False
        
        def binarySearch(array, target, left=None, right=None):
            if left is None:
                left, right = 0, len(array) - 1
            
            if left > right:
                return False
            
            mid = int((left + right) / 2)
            if array[mid] == target:
                return True
            elif array[mid] < target:
                return binarySearch(array, target, mid + 1, right)
            else:
                return binarySearch(array, target, left, mid - 1)
        
#         def binarySearch(array, target):
#             left, right = 0, len(array) - 1
            
#             while left <= right:
#                 mid = int((left + right) / 2)
                
#                 if array[mid] == target:
#                     return True
#                 elif array[mid] < target:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
            
#             return False
        
        for row in matrix:
            if row[0] <= target <= row[-1] and binarySearch(row, target):
                return True
        return False




####################################################################################################
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
        