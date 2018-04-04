# https://leetcode.com/problems/powx-n/description/
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0: return 1
        if n < 0:
            n = -n
            x = 1 / x

        result = 1

        while n > 1:
            if n & 0x1 == 0x1:
                result *= x
            n >>= 1
            x *= x

        return result * x

s = Solution()
print(s.myPow(2.1, 3))