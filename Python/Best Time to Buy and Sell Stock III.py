class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        profits = []
        min_price = 2 ** 31 - 1
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
            profits.append(max_profit)
        
        max_price = 0
        ans = profits[-1]
        for index in range(len(prices) - 1, 0, -1):
            max_price = max(max_price, prices[index])
            ans = max(ans, max_price - prices[index] + profits[index - 1])
        return ans