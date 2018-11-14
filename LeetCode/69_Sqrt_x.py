# https://leetcode.com/problems/sqrtx/
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        left, right = 1, x // 2
        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 > x:
                right = mid - 1
            elif (mid + 1) ** 2 > x:
                return mid
            else:
                left = mid + 1

