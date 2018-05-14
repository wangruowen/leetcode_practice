# https://leetcode.com/problems/sum-of-square-numbers/description/
import math

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        # c must also be a perfect square
        a = int(math.sqrt(c / 2))
        while True:
            if c < a**2:
                break
            b_raw = math.sqrt(c - a**2)
            if int(b_raw) == b_raw:
                return True
            a += 1

        return False
