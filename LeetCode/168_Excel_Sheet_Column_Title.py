# https://leetcode.com/problems/excel-sheet-column-title/
class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        # Base 26, 0-25 as A-Z, like Base 10 or Base 2
        result = ""
        while n > 0:
            n -= 1  # for every bit, we need to count from 0-25, minus the carry bit
            result = chr(ord('A') + n % 26) + result
            n //= 26
        return result

s = Solution()
print(s.convertToTitle(53))