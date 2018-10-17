# https://leetcode.com/problems/arranging-coins/description/
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n >= count:
            n -= count
            count += 1
        return count - 1