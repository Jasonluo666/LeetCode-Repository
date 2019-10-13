def  seeCows(cows):
    if len(cows) < 2:
        return 0
    
    stack = [0]
    index = 1
    ans = 0
    while index < len(cows):
        while stack and cows[index] >= cows[stack[-1]]:
            short_index = stack.pop()
            ans += index - short_index - 1
        
        stack.append(index)
        index += 1
    
    while stack:
        short_index = stack.pop()
        ans += len(cows) - short_index - 1
    
    return ans