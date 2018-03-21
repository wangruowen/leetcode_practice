# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0: return 0

        min_price, max_profit = prices[0], 0
        for cur_price in prices:
            if min_price > cur_price:
                min_price = cur_price
            else:
                profit = cur_price - min_price
                if max_profit < profit:
                    max_profit = profit
        return max_profit