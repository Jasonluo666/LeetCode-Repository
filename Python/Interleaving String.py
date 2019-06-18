class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        self.cache = {}
        def dfs(s1, s2, s3):
            if (not s1 and not s2) or not s3:
                if not s1 and not s2 and not s3:
                    return True
                else:
                    return False
            
            if (s1, s2, s3) in self.cache:
                return self.cache[(s1, s2, s3)]
            
            ans = False
            if len(s1) > 0 and s1[0] == s3[0]:
                ans = ans or dfs(s1[1:], s2, s3[1:])
            if len(s2) > 0 and s2[0] == s3[0]:
                ans = ans or dfs(s1, s2[1:], s3[1:])
            
            self.cache[(s1, s2, s3)] = ans
            return ans
        return dfs(s1, s2, s3)