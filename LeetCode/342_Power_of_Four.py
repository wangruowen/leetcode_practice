# https://leetcode.com/problems/power-of-four/description/
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # bit manipulation
        # power of 4 means power of 2 with even number of power
        count = 0
        if num <= 0:
            return False
        while num > 1:
            if num & 1 == 1:
                return False
            num >>= 1
            count += 1
        return count % 2 == 0

s = Solution()
print(s.isPowerOfFour(5))
