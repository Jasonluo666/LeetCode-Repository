def  calculateMinimumHP(dungeon):
    if not dungeon or not dungeon[0]:
        return 1
    
    dp = [[0 for _ in range(len(dungeon[0]))] for _ in range(len(dungeon))]

    if dungeon[-1][-1] >= 0:
        dp[-1][-1] = 1
    else:
        dp[-1][-1] = -dungeon[-1][-1] + 1
    
    for x in range(len(dungeon) - 2, -1, -1):
        dp[x][-1] = dp[x + 1][-1] - dungeon[x][-1]
        if dp[x][-1] <= 0:
            dp[x][-1] = 1
    for y in range(len(dungeon[-1]) - 2, -1, -1):
        dp[-1][y] = dp[-1][y + 1] - dungeon[-1][y]
        if dp[-1][y] <= 0:
            dp[-1][y] = 1

    for x in range(len(dungeon) - 2, -1, -1):
        for y in range(len(dungeon[0]) - 2, -1, -1):
            dp[x][y] = min(dp[x + 1][y], dp[x][y + 1]) - dungeon[x][y]
            if dp[x][y] <= 0:
                dp[x][y] = 1
    
    return dp[0][0]


# def  calculateMinimumHP(dungeon):
#     if not dungeon or not dungeon[0]:
#         return 1
    
#     dp = [[0 for _ in range(len(dungeon[0]))] for _ in range(len(dungeon))]
#     # track = [[None for _ in range(len(dungeon[0]))] for _ in range(len(dungeon))]
#     track_hp = [[None for _ in range(len(dungeon[0]))] for _ in range(len(dungeon))]

#     dp[0][0] = dungeon[0][0]
#     # track[0][0] = [(0, 0)]
#     track_hp[0][0] = dungeon[0][0]
    
#     for x in range(1, len(dungeon)):
#         dp[x][0] = dp[x - 1][0] + dungeon[x][0]
#         # track[x][0] = track[x - 1][0] + [(x, 0)]
#         track_hp[x][0] = min(track_hp[x - 1][0], dp[x][0])
#     for y in range(1, len(dungeon[0])):
#         dp[0][y] = dp[0][y - 1] + dungeon[0][y]
#         # track[0][y] = track[0][y - 1] + [(0, y)]
#         track_hp[0][y] = min(track_hp[0][y - 1], dp[0][y])
    
#     for x in range(1, len(dungeon)):
#         for y in range(1, len(dungeon[0])):
#             if(track_hp[x - 1][y] >= track_hp[x][y - 1]):
#                 dp[x][y] = dp[x - 1][y] + dungeon[x][y]
#                 # track[x][y] = track[x - 1][y] + [(x, y)]
#                 track_hp[x][y] = min(track_hp[x - 1][y], dp[x][y])
#             else:
#                 dp[x][y] = dp[x][y - 1] + dungeon[x][y]
#                 # track[x][y] = track[x][y - 1] + [(x, y)]
#                 track_hp[x][y] = min(track_hp[x][y - 1], dp[x][y])

#     # min_hp = None
#     # for path in track[-1][-1]:
#     #     if min_hp is None or min_hp > dp[path[0]][path[1]]:
#     #         min_hp = dp[path[0]][path[1]]

#     if track_hp[-1][-1] >= 0:
#         return 1
#     else:
#         return -track_hp[-1][-1] + 1
