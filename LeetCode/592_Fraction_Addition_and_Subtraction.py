# https://leetcode.com/problems/fraction-addition-and-subtraction/description/
import re
from fractions import Fraction

class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        result = Fraction(0, 1)
        pattern = re.compile(r'(\+|-)?(\d+/\d+)')
        for m in re.finditer(pattern, expression):
            op, frac = m.group(1), m.group(2)
            # print(m.groups())
            if not op or op == "+":
                result += Fraction(frac)
            else:
                result -= Fraction(frac)
            # print(result)
        numerator, denominator = result.numerator, result.denominator
        result_str = str(numerator)
        if denominator == 1:
            result_str += "/1"
        else:
            result_str += "/" + str(denominator)
        return result_str

s = Solution()
expre = "-5/2+10/3+7/9"
print(s.fractionAddition(expre))
