# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/
class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        # Follow the DP equation listed in the following post
        # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108870/most-consistent-ways-of-dealing-with-the-series-of-stock-problems
        # T[i][k][0] = max(T[i-1][k][0], T[i-1][k][1] + prices[i])
        # T[i][k][1] = max(T[i-1][k][1], T[i-1][k][0] - prices[i] - fee)
        T_ik0, T_ik1 = 0, float('-inf')
        for each in prices:
            old_T_ik0 = T_ik0
            T_ik0 = max(T_ik0, T_ik1 + each)
            T_ik1 = max(T_ik1, old_T_ik0 - each - fee)
        return T_ik0