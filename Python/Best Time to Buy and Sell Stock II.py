class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if not prices:
            return 0
        
        profit = 0
        for index in range(1, len(prices)):
            if prices[index] > prices[index-1]:
                profit += prices[index] - prices[index-1]
        
        return profit