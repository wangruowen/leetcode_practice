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

    def findNthDigit_v2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10:
            return n

        i = 1
        cur = i * 9 * 10 ** (i - 1)
        while n > cur:
            n -= cur
            i += 1
            cur = i * 9 * 10 ** (i - 1)

        latest_num = 10 ** (i - 1) - 1 + n // i
        # print(latest_num)
        if n % i == 0:
            return latest_num % 10
        latest_num += 1
        latest_num //= 10 ** (i - n % i)
        return latest_num % 10


s = Solution()
print(s.findNthDigit_v2(12))


