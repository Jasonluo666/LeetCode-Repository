# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n < 1:
            return -1
        
        ans = 0
        # if he knows others -> switch
        for i in range(n):
            if knows(ans, i):
                ans = i
        
        # check if he knows (0, him - 1)
        for j in range(ans):
            if knows(ans, j):
                return -1
        
        # check if everybody knows him
        for k in range(n):
            if not knows(k, ans):
                return -1
        
        return ans