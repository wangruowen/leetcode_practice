__author__ = 'ruowen.wang'
# https://leetcode.com/problems/power-of-two/

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        found_one = False
        if n <= 0: return False
        for _ in range(32):
            if n & 1 == 1:
                if not found_one:
                    found_one = True
                else:
                    return False
            n >>= 1
        return found_one