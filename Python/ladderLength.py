def helper(word1, word2):
    count = sum([word1[i] != word2[i] for i in range(len(word1))])
    return count == 1

# def dfs(current, endWord, wordList, step):
#     global ans
#     if current == endWord:
#         if ans is None or ans > step:
#             ans = step
#         return
    
#     if step == len(wordList) + 1 or (ans is not None and step >= ans):
#         return
    
#     for index in range(len(wordList)):
#         if wordList[index] is not None and helper(wordList[index], current):
#             temp = wordList[index]
#             wordList[index] = None
#             dfs(temp, endWord, wordList, step + 1)
#             wordList[index] = temp

def bfs(beginWord, endWord, wordList):
    queue = [(beginWord, 1)]

    while queue:
        next, step = queue[0]
        queue = queue[1:]

        if next == endWord:
            return step
        for index in range(len(wordList)):
            if wordList[index] is not None and helper(wordList[index], next):
                queue.append((wordList[index], step + 1))
                wordList[index] = None
    return 0

def  ladderLength(beginWord, endWord, wordList):
    global ans
    ans = None
    
    # dfs(beginWord, endWord, wordList, 1)
    # if ans is None:
    #     return 0
    # return ans
    return bfs(beginWord, endWord, wordList)

print(ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))