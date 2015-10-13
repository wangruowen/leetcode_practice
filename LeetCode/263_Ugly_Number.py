__author__ = 'Ruowen'
# https://leetcode.com/problems/ugly-number/

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0: return False
        if num == 1: return True

        for each_prime in (2, 3, 5):
            if num % each_prime == 0:
                while num % each_prime == 0:
                    num /= each_prime
        return True if num == 1 else False