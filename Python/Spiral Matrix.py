class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        
        count = len(matrix) * len(matrix[0])
        
        x, y = 0, 0
        # two boolean flags -> control direction
        horizontal, vertical = False, False
        ans = []
        flag = False
        
        while count > 0:
            # whether need to change the direction
            if flag == False:
                count -= 1
                ans.append(matrix[x][y])
                matrix[x][y] = None
            else:
                flag = False
            
            if horizontal == vertical == False:
                if y + 1 == len(matrix[0]) or matrix[x][y + 1] == None:
                    horizontal = True
                    flag = True
                else:
                    y += 1
            elif horizontal == True and vertical == False:
                if x + 1 == len(matrix) or matrix[x + 1][y] == None:
                    vertical = True
                    flag = True
                else:
                    x += 1
            elif horizontal == vertical == True:
                if y - 1 < 0 or matrix[x][y - 1] == None:
                    horizontal = False
                    flag = True
                else:
                    y -= 1
            elif horizontal == False and vertical == True:
                if x - 1 < 0 or matrix[x - 1][y] == None:
                    vertical = False
                    flag = True
                else:
                    x -= 1
            
        return ans