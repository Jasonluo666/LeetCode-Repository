class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        import heapq
        heap = []
        ans = []
        
        def dist(point):
            return point[0] ** 2 + point[1] ** 2
        
        for index in range(len(points)):
            heapq.heappush(heap, (dist(points[index]), index, points[index]))
        
        for _ in range(K):
            _, _, point = heapq.heappop(heap)
            ans.append(point)
        
        return ans