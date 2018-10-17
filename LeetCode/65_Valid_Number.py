# https://leetcode.com/problems/valid-number/
import re

class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if re.match(r'^\s*[\+-]?((\d+(\.\d*)?)|(\.\d+))([eE][\+-]?\d+)?\s*$', s):
            return True
        return False

s = Solution()
test = ["0", " 0.1 ", ".1", " 10 ", " -1 ", "+1", "0.1234e234"]
for i in test:
    print(s.isNumber(i))
