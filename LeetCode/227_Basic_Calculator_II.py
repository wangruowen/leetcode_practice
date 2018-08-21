# https://leetcode.com/problems/basic-calculator-ii/description/
import operator

class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        result, op, cur_num, stack = 0, None, 0, []
        s += "+0"
        for c in s:
            if c == ' ':
                continue
            elif c.isdigit():
                cur_num = 10 * cur_num + int(c)
            elif c in "+-":
                # if we see +-, then the previous op always happen
                if op in [operator.mul, operator.floordiv]:
                    result = op(result, cur_num)
                    # If there is op before the */, we pop it and calculate
                    if len(stack) > 0:
                        prev_result, prev_op = stack.pop()
                        result = prev_op(prev_result, result)
                elif op:
                    result = op(result, cur_num)
                else:
                    result = cur_num
                cur_num = 0
                op = operator.add if c == '+' else operator.sub
            elif c in "*/":
                # if we see */, and previous op is "+-", then we push stack
                if op in [operator.add, operator.sub]:
                    stack.append([result, op])
                    result = cur_num
                elif op:
                    result = op(result, cur_num)
                else:
                    result = cur_num
                op = operator.mul if c == '*' else operator.floordiv
                cur_num = 0

        return result

s = Solution()
S = "3/2 + 1*6 -1"
print(s.calculate(S))






