class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        base = 1
        ans = [0 for x in range(num + 1)]
        for index in range(1, num + 1):
            if index - base >= base:
                base *= 2
            ans[index] = 1 + ans[index - base]
        
        return ans