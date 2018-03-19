# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/
import sys

class StockState(object):
    def __init__(self, profit, done_trans):
        self.profit = profit
        self.done_trans = done_trans

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        # f[i][k] is an array that keep the max profit after k th transactions till Day i
        # Given Day i, there can be two states:
        # 1. End with Sell:
        #   profit_end_sell[i][k] = max(profit_end_sell[i - 1][k],
        #                               profit_end_buy[i - 1][k - 1] + cur_price)
        #
        # 2. End with Buy:
        #   profit_end_buy[i][k] = max(profit_end_buy[i - 1][k],
        #                              profit_end_sell[i - 1][k] - cur_price)
        profit_buy, profit_sell = [StockState(-sys.maxint, 0)], [StockState(0, 0)]

        for cur_price in prices:
            for cur_profit_buy, done_trans in profit_buy:

            for k in range(k_so_far + 1):
                prev_buy[k] = profit_buy[k]
                profit_buy[k] = max(prev_buy[k], prev_sell[k] - cur_price)

                prev_sell[k] = profit_sell[k]
                if prev_buy[k] + cur_price > prev_sell[k]:
                    k_so_far = k + 1
                    profit_sell[k_so_far] = prev_buy[k] + cur_price
                else:
                    profit_sell[k] = prev_sell[k]

        return max(profit_sell)

s = Solution()
a = [1,4,2]
print(s.maxProfit(a))


