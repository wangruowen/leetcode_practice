# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0  # As we require at least 3 days for buy, sell, cooldown

        # For DP, we need to carefully define variables and equations
        # buy[i] means till Day i, the total profit that ends with a buy (not closed transaction)
        # buy[i] = max(sell[i - 2] - cur_price, buy[i - 1])
        # buy[i] can be either the last sell two days ago due to cooldown, or keep holding as yesterday's buy

        # sell[i] means till Day i, the total profit that ends with a sell
        # sell[i] = max(sell[i - 1], buy[i - 1] + cur_price)
        # sell[i] can be either yesterday's sell, with cooldown, or sell today on Day i

        profit_end_w_buy, profit_end_w_sell = [None] * len(prices), [None for _ in range(len(prices))]
        profit_end_w_buy[0] = -prices[0]  # Because this has to be end with a buy, buy[0] = 0 - prices[0]
        profit_end_w_sell[0] = 0
        for i in range(1, len(prices)):
            cur_price = prices[i]
            profit_end_w_buy[i] = max((profit_end_w_sell[i - 2] if i > 1 else 0) - cur_price,
                                      profit_end_w_buy[i - 1])
            profit_end_w_sell[i] = max(profit_end_w_sell[i - 1], profit_end_w_buy[i - 1] + cur_price)

        # print(profit_end_w_buy)
        # print(profit_end_w_sell)
        return profit_end_w_sell[-1]


s = Solution()
a=[1, 2, 4]
print(s.maxProfit(a))