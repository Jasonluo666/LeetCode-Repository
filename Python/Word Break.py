class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True
        if not wordDict:
            return False
        
        cache = {s:True}
        queue = [s]
        max_word_len = max([len(w) for w in wordDict])
        
        while len(queue) > 0:
            deque = queue[0]
            queue = queue[1:]
            
            for end in range(1, max_word_len + 1):
                if end > len(deque):
                    break
                if deque[:end] in wordDict:
                    possbile_replace = deque[end:]
                    if len(possbile_replace) == 0:
                        return True
                    if possbile_replace not in cache:
                        cache[possbile_replace] = True
                        queue.append(possbile_replace)
        return False