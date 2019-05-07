class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        # tracking the local min/max
        local_min = local_max = prices[0]
        ans = 0
        
        for element in prices:
            if element > local_max:
                local_max = element
            elif element < local_min:
                ans = max(ans, local_max - local_min)
                local_min = local_max = element
        return max(ans, local_max - local_min)