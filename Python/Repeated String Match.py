class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        
        if not B:
            return 0
        elif not A:
            return -1
        
        # create valid ans
        count = 0
        ans = ""
        while len(ans) < len(B):
            ans += A
            count += 1
        
        # possible ans -> len(A) + len(B)
        if B in ans:
            return count
        elif B in ans + A:
            return count + 1
        else:
            return -1