# https://leetcode.com/problems/score-of-parentheses/description/
class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        # The key thing is what we store on the stack
        cur_score, stack = 0, []
        for c in S:
            if c == '(':
                stack.append(c)  # push '(' as a frame separator like func call frames
            elif c == ')':
                nested_val = 0
                while type(stack[-1]) is int:
                    nested_val += stack.pop()
                stack.pop()  # pop out the '('
                if nested_val == 0:
                    nested_val = 1
                else:
                    nested_val *= 2
                stack.append(nested_val)

        result = 0
        while len(stack) > 0:
            result += stack.pop()

        return result

s = Solution()
S = "(()(()))"
print(s.scoreOfParentheses(S))
