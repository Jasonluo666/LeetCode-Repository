class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        
        self.partition = []
        self.dfs(s, [])
        return self.partition
        
    
    def isPal(self, s):
        return s == s[::-1]
    
    def dfs(self, s, ans):
        if not s:
            self.partition.append(ans)
            return
        
        for index in range(1, len(s) + 1):
            if self.isPal(s[:index]):
                self.dfs(s[index:], ans + [s[:index]])