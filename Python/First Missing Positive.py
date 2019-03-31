class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        import heapq
        
        heapq.heapify(nums)
        ans = 1
        while len(nums) > 0:
            next_num = heapq.heappop(nums)
            # handle negative and identical values
            if next_num <= 0 or ans == next_num + 1:
                continue
            
            # check missing integer -> O(n)
            if ans == next_num:
                ans += 1
            else:
                break
        
        return ans