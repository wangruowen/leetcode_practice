# https://leetcode.com/problems/binary-number-with-alternating-bits/description/
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        last = None
        while n != 0:
            cur = n & 1
            if last is not None and cur == last:
                return False
            last = cur
            n >>= 1
        return True