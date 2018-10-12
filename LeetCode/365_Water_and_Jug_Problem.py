# https://leetcode.com/problems/water-and-jug-problem/
import math

class Solution:
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if z == 0:
            return True

        # We need to check two conditions
        # 1. x + y >= z
        if x + y < z:
            return False

        # 2. ax + by = z
        # Let k = gcd(x, y)
        # ax + by = aki + bkj = k(ai + bj) = z
        if z % math.gcd(x, y) == 0:
            return True

        return False