class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        
        from collections import Counter
        counter = Counter(J)
        ans = 0
        for element in S:
            if element in counter:
                ans += 1
        return ans