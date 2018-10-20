class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        
        # depth first search for all possibilities
        def dfs(s='', left=0, right=0):
            if len(s) == 2 * n:
                ans.append(s)
            else:
                if left > right:
                    dfs(s+')', left, right+1)
                if left < n:
                    dfs(s+'(', left+1, right)
        
        dfs()
        
        return ans