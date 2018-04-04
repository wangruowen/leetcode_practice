# https://leetcode.com/problems/divide-two-integers/description/

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # First, handle corner case
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1

        if divisor == 0 or (dividend == INT_MIN and divisor == -1):
            return INT_MAX
        if dividend < 0 and divisor < 0 or dividend >= 0 and divisor > 0:
            is_neg = False
        else:
            is_neg = True

        dividend = abs(dividend)
        divisor = abs(divisor)

        total_quotient = 0
        while dividend >= divisor:
            cur_divisor = divisor
            quotient = 1
            while dividend >= (cur_divisor << 1):
                cur_divisor <<= 1
                quotient <<= 1
            dividend -= cur_divisor
            total_quotient += quotient

        if is_neg:
            return -total_quotient
        else:
            return total_quotient