# https://leetcode.com/problems/count-numbers-with-unique-digits/description/
import math

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n == 1:
            return 10
        # num of (0 <= x < 10**n) = num of (0 <= x < 10) + num of (10 <= x < 10**2) + ... + (10**(n - 1) <= x < 10**n)
        return self._helper(n - 1, n) + self.countNumbersWithUniqueDigits(n - 1)

    def _helper(self, start, end):
        # Number of digits in this range is (start + 1)
        if start + 1 > 10:
            # If the num of digits is bigger than 10, there will always be dup digits
            return 0
        # leading digit is from 1 to 9
        return 9 * math.factorial(9) / math.factorial(9 - start)
