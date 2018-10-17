# https://leetcode.com/problems/bitwise-and-of-numbers-range/
# Given a range [m, n] where 0 <= m <= n <= 2147483647,
# return the bitwise AND of all numbers in this range, inclusive.
#
# Example 1:
#
# Input: [5,7]
# Output: 4
# Example 2:
#
# Input: [0,1]
# Output: 0
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # Tricky
        # last bit of (odd number & even number) is 0.
        # when m != n, There is at least an odd number and an even number, so the last bit position result is 0.
        # Move m and n right a position.
        if m == 0:
            return 0

        result = 1
        while m != n:
            m >>= 1
            n >>= 1
            result <<= 1
        return result * m



