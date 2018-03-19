# https://leetcode.com/problems/nth-digit/description/
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        while True:
            if n > 0:
                if n > len(str(i)):
                    n -= len(str(i))
                else:
                    return int(str(i)[n - 1])
            i += 1

