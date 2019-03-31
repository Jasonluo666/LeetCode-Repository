class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        import heapq
        
        # maintain two heap -> max/min heap -> alway find median at the top
        self.max_heap = []
        self.min_heap = []
        heapq.heapify(self.max_heap)
        heapq.heapify(self.min_heap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.min_heap, num)
        heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        
        if len(self.min_heap) < len(self.max_heap):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            ans = (heapq.nsmallest(1, self.min_heap)[0] - heapq.nsmallest(1, self.max_heap)[0]) / 2
        else:
            ans = heapq.nsmallest(1, self.min_heap)[0]
        return ans


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()