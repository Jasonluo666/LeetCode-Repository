class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if not prices:
            return 0
        
        ans_min = ans_max = prices[0]
        ans = 0
        for element in prices:
            if element > ans_max:
                ans_max = element
            
            if element < ans_min:
                ans = max(ans, ans_max - ans_min)
                ans_min = element
                ans_max = element
        
        ans = max(ans, ans_max - ans_min)
        return ans