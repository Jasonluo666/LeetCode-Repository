def  superSeq(X, Y):
    X = " " + X
    Y = " " + Y

    dp = [[None for _ in range(len(Y))] for _ in range(len(X))]

    dp[0][0] = " "
    
    for i in range(1, len(X)):
        dp[i][0] = dp[i - 1][0] + X[i]
    
    for j in range(1, len(Y)):
        dp[0][j] = dp[0][j - 1] + Y[j]
    
    for i in range(1, len(X)):
        for j in range(1, len(Y)):
            if X[i] == Y[j]:
                dp[i][j] = dp[i - 1][j - 1] + X[i]
            
            if len(dp[i - 1][j]) <= len(dp[i][j - 1]):
                temp = dp[i - 1][j] + X[i]
            else:
                temp = dp[i][j - 1] + Y[j]

            if dp[i][j] is None or len(dp[i][j]) > len(temp):
                dp[i][j] = temp
    
    return dp[-1][-1][1:]

print(superSeq("AGGTAB", "GXTXAYB"))