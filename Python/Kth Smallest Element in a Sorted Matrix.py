class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        # create a heap to find the kth largest/smallest element
        import heapq
        
        heap = []
        for x in matrix:
            for y in x:
                heapq.heappush(heap, y)
        
        while k != 0:
            ans = heapq.heappop(heap)
            k -= 1
        
        return ans
        