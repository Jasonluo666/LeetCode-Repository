class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        # ans = (m + n)! / m! * n!
        # combination problem
        factorial_mn = 1
        factorial_m = 1
        factorial_n = 1
        
        for x in range(1, m + n - 1):
            factorial_mn *= x
        
        for x in range(1, m):
            factorial_m *= x
        
        for x in range(1, n):
            factorial_n *= x
        
        return int(factorial_mn / (factorial_m * factorial_n))