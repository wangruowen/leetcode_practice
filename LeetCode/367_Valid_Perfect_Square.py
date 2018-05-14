# https://leetcode.com/problems/valid-perfect-square/description/
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # Binary search
        low, high = 1, num
        while low <= high:
            mid = (low + high) / 2
            square_mid = mid * mid
            if square_mid == num:
                return True
            elif square_mid < num:
                low = mid + 1
            else:
                high = mid - 1
        return False