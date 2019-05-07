class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if not matrix or len(matrix[0]) == 0:
            return False
        
        def binarySearch(array, target):
            left, right = 0, len(array) - 1
            
            while left <= right:
                mid = int((left + right) / 2)
                
                if array[mid] == target:
                    return True
                elif array[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False
        
        
        for row in matrix:
            if row[0] <= target <= row[-1]:
                return binarySearch(row, target)
        
        return False