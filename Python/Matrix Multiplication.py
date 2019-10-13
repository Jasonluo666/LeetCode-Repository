def find_valid(p, index):
    left = index - 1
    while left > 0:
        if p[left] != -1:
            break
        left -= 1
    
    right = index + 1
    while right < len(p) - 1:
        if p[right] != -1:
            break
        right += 1
    return left, right

def dfs(p, val, remain):
    global ans
    if remain < 3 or ans < val:
        ans = min(ans, val)
        return

    for index in range(1, len(p) - 1):
        if p[index] != -1:
            left, right = find_valid(p, index)
            
            temp = p[index]
            p[index] = -1
            dfs(p, val + temp * p[left] * p[right], remain - 1)
            p[index] = temp

def DP(p):
    dp = [[2 ** 31 - 1 for _ in range(len(p))] for _ in range(len(p))]

    for x in range(len(p)):
        dp[x][x] = 0
        if x > 0:
            dp[x - 1][x] = 0

    for length in range(2, len(p)):
        for x in range(len(p) - length):
            for k in range(x + 1, x + length):
                dp[x][x + length] = min(dp[x][x + length], dp[x][k] + dp[k][x + length] + p[x] * p[k] * p[x + length])
    return dp[0][-1]

def  getMatrixChain(p): 
    if len(p) < 3:
        return 0

    global ans 
    ans = 2 ** 31 - 1
    dfs(p, 0, len(p))
    return ans


# DP and DFS solutions
print(getMatrixChain([40, 20, 30, 10, 30, 100]))
print(DP([40, 20, 30, 10, 30, 100]))