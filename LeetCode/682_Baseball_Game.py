# https://leetcode.com/problems/baseball-game/description/
import re

class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        for each in ops:
            new_point = 0
            if re.match(r'-?[0-9]+', each):
                new_point = int(each)
            elif each == "+":
                if len(stack) >= 2:
                    new_point = stack[-1] + stack[-2]
            elif each == "D":
                new_point = 2 * stack[-1]
            elif each == "C":
                stack.pop()
            if new_point != 0:
                stack.append(new_point)
        return sum(stack)

s = Solution()
a = ["5","-2","4","C","D","9","+","+"]
print(s.calPoints(a))

