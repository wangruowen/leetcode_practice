# https://leetcode.com/problems/guess-number-higher-or-lower/description/
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num):
    return 0

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 1, n
        while start <= end:
            mid = (start + end) / 2
            guess_result = guess(mid)
            if guess_result == 0:
                return mid
            elif guess_result < 0:
                end = mid
            else:
                start = mid + 1