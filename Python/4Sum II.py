class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        
        import collections
        
        if not A:
            return 0
        
        # initialize Counter -> hash with element start with 0
        AB = collections.Counter()
        for a in A:
            for b in B:
                # do not need to initialize, simply manipulate the value
                AB[a+b] += 1
        
        return sum(AB[-(c+d)] for c in C for d in D)