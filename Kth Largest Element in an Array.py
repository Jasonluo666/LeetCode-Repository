class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        import heapq
        
        heapq.heapify(nums)
        ans = None
        for _ in range(len(nums) - k + 1):
            ans = heapq.heappop(nums)
        
        return ans