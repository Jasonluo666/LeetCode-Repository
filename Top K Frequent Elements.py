class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        import heapq
        
        if not nums:
            return []
        
        hash_table = {}
        # calculate the frequency O(n)
        for element in nums:
            if element in hash_table.keys():
                hash_table[element] += 1
            else:
                hash_table[element] = 1
        
        # store the element into heap -> use negative value for max heap O(n)
        heap = [(-hash_table[x], x) for x in hash_table.keys()]
        heapq.heapify(heap)
        
        # O(n)
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        
        return ans