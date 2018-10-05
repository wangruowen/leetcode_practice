# https://leetcode.com/problems/add-digits/
class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # 999 => 27 => 9
        # 89 => 17 => 8, 98 % 9 = 8
        # 79 => 16 => 7
        if num == 0:
            return 0

        if num % 9 == 0:
            return 9
        else:
            return num % 9