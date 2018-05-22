# https://leetcode.com/problems/factorial-trailing-zeroes/description/
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # O(log n)
        # Count how many 5s
        return n / 5 + self.trailingZeroes(n / 5) if n >= 5 else 0