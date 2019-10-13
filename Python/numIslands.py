def floodFill(grids, x, y):
    if not (0 <= x < len(grids) and 0 <= y < len(grids[0])) or grids[x][y] == 0:
        return 0
    
    grids[x][y] = 0
    return 1 + floodFill(grids, x - 1, y) + floodFill(grids, x + 1, y) + floodFill(grids, x, y - 1) + floodFill(grids, x, y + 1)

def  numIslands(grids):
    if not grids or not grids[0]:
        return 0

    ans = {}
    for x in range(len(grids)):
        for y in range(len(grids[0])):
            if grids[x][y]:
                ans[floodFill(grids, x, y)] = True
    
    return len(ans.keys())