class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        
        hashmap = {}
        self.num = 0
        
        def dfs(x, y, stones):
            if (x, y) in hashmap:
                return
            
            hashmap[(x, y)] = True
            for stone in stones:
                if (stone[0], stone[1]) not in hashmap and (x == stone[0] or y == stone[1]):
                    self.num += 1
                    dfs(stone[0], stone[1], stones)
        
        for stone in stones:
            dfs(stone[0], stone[1], stones)
        return self.num