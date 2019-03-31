class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        # hash set of input
        cache = set(nums)
        ans = 1
        for element in cache:
            # find every first element of possible ans
            if element - 1 not in cache:
                local_max = 0
                while element in cache:
                    local_max += 1
                    element += 1
               
                ans = max(ans, local_max)
        
        return ans