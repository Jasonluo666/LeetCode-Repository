def dfs(current, words, path):
    if not current:
        return len(path) > 1
    
    for word in words:
        if word is None:
            continue
        
        if len(current) >= len(word) and word == current[: len(word)]:
            if word not in path:
                path[word] = True
                if dfs(current[len(word):], words, path):
                    return True
                del path[word]
            else:
                if dfs(current[len(word):], words, path):
                    return True
    return False

def  findAllConcatenated(words):
    ans = []
    for index in range(len(words)):
        temp = words[index]
        words[index] = None

        if dfs(temp, words, {}):
            ans.append(temp)
        
        words[index] = temp
    return ans

print(findAllConcatenated(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))