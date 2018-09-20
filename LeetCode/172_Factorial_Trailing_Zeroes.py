# https://leetcode.com/problems/factorial-trailing-zeroes/
class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Count 5s
        # E.g, 5, 10, 15, ..., 100
        #   (1) 1, 2, .., 5, ... 10, .., 15, .. 20
        #   (2) Reduce n from 100 to 20, now continue to count 5 in 20
        # First, count how many i <= n and i % 5 == 0
        # Second, count how many i <= n // 5 and i % 5 == 0
        # Until n == 1
        counts = 0
        while n > 1:
            counts += n // 5
            n //= 5
        return counts
