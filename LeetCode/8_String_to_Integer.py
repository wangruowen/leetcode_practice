# https://leetcode.com/problems/string-to-integer-atoi/description/
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if len(str) == 0:
            return 0

        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        is_neg = False
        if str[0] == "+":
            str = str[1:]
        elif str[0] == "-":
            is_neg = True
            str = str[1:]
        result = 0
        for c in str:
            if c.isdigit():
                result = result * 10 + int(c)
            else:
                break

        if is_neg:
            result = -result

        if result > INT_MAX:
            result = INT_MAX
        if result < INT_MIN:
            result = INT_MIN

        return result

s = Solution()
ss = "-91283472332"
print(s.myAtoi(ss))