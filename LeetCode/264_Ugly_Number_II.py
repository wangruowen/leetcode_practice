__author__ = 'Ruowen'
# https://leetcode.com/problems/ugly-number-ii/

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0: return None
        if n == 1: return 1

        # order 2, 3, 4, 5
        orders = {'2': 0, '3': 0, '4': 0, '5': 0}
        i = 0
        while True:
            for each_order in ('2', '3', '4', '5'):
                orders[each_order] += 1
                i += 1
                if i == n - 1:
                    return pow(2, orders['2']) * pow(3, orders['3']) * pow(4, orders['4']) * pow(5, orders['5'])
