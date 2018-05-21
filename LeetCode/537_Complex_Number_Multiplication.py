# https://leetcode.com/problems/complex-number-multiplication/description/
import re

class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        match = re.match(r'^(-?\d*)\+(-?\d*)i$', a)
        a_real, a_imag = int(match.group(1)), int(match.group(2))
        match = re.match(r'^(-?\d*)\+(-?\d*)i$', b)
        b_real, b_imag = int(match.group(1)), int(match.group(2))
        c_real = a_real * b_real - a_imag * b_imag
        c_imag = a_imag * b_real + a_real * b_imag
        return "%d+%di" % (c_real, c_imag)

s = Solution()
a="78+-76i"
b="-86+72i"
print(s.complexNumberMultiply(a, b))