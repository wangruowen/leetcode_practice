# https://leetcode.com/problems/base-7/description/
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        # 100 = 2 * 7**2 + 0 * 7**1 + 2 * 7**0
        #     = (2*7**1 + 0*7**0) * 7 + 2
        result = ""
        if num < 0:
            result = "-"
            num = abs(num)
        if num >= 7:
            result += self.convertToBase7(num // 7)
        result += str(num % 7)

        return result

s = Solution()
print(s.convertToBase7(-7))
