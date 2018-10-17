# https://leetcode.com/problems/basic-calculator/
import operator

class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        cur_num, sign = 0, 1
        result, stack = 0, []
        for c in s:
            if c == ' ':
                continue
            elif c.isdigit():
                cur_num = 10 * cur_num + int(c)
            elif c == '+':
                result += sign * cur_num
                cur_num = 0
                sign = 1
            elif c == '-':
                result += sign * cur_num
                cur_num = 0
                sign = -1
            elif c == '(':
                # Temp save current result and sign
                stack.append([result, sign])
                result, sign = 0, 1
            elif c == ')':
                result += sign * cur_num
                cur_num, sign = 0, 1
                prev_result, prev_sign = stack.pop()
                prev_result += prev_sign * result
                result = prev_result

        return result + sign * cur_num

