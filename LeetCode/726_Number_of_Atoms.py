# https://leetcode.com/problems/number-of-atoms/description/
import re
from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        parser = re.findall(r"([A-Z][a-z]*)(\d*)|(\()|(\))(\d*)", formula)
        stack = [defaultdict(int)]
        for name, m1, left_open, right_close, m2 in parser:
            if name:
                stack[-1][name] += int(m1 or 1)
            if left_open:
                stack.append(defaultdict(int))
            if right_close:
                for k, v in stack.pop().items():
                    stack[-1][k] += v * int(m2 or 1)
        return "".join([name + (str(stack[-1][name]) if stack[-1][name] > 1 else "") for name in sorted(stack[-1])])