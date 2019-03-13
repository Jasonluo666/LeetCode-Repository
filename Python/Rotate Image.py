class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        
        # rotate nums at each level
        n = len(matrix) - 1
        current = int(n / 2)
        while current >= 0:
            for index in range(n - current * 2):
                # nums on four sides
                matrix[current][current + index], matrix[current + index][n - current], matrix[n - current][n - current - index], matrix[n - current - index][current] = matrix[n - current - index][current], matrix[current][current + index], matrix[current + index][n - current], matrix[n - current][n - current - index]
            current -= 1