class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        dp_table = [2 ** 31 - 1 for x in range(amount + 1)]
        dp_table[0] = 0
        for index in range(1, amount + 1):
            for option in coins:
                if index - option < 0:
                    continue
                dp_table[index] = min(dp_table[index], dp_table[index - option] + 1)
        if dp_table[-1] == 2 ** 31 - 1:
            return -1
        else:
            return dp_table[-1]