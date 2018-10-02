# https://leetcode.com/problems/fraction-to-recurring-decimal/
class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        is_neg = False
        if (numerator > 0 and denominator < 0) or (numerator < 0 and denominator > 0):
            is_neg = True
        numerator, denominator = abs(numerator), abs(denominator)

        result = str(numerator // denominator)
        numerator %= denominator
        lookup = {}
        if numerator > 0:
            result += "."

        while numerator > 0 and numerator not in lookup:
            lookup[numerator] = len(result)
            numerator *= 10
            quotient, remainder = divmod(numerator, denominator)
            result += str(quotient)
            numerator = remainder

        if numerator in lookup:
            # non-repeat and repeat are divided by the first time the lookup[numerator] occurs
            result = result[:lookup[numerator]] + "(" + result[lookup[numerator]:] + ")"

        if is_neg:
            result = "-" + result

        return result

s = Solution()
print(s.fractionToDecimal(-50, 8))